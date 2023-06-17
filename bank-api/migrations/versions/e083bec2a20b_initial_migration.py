"""Initial migration.

Revision ID: e083bec2a20b
Revises: 
Create Date: 2023-06-16 23:33:51.257180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e083bec2a20b'
down_revision = None
branch_labels = None
depends_on = None

create_trigger = """
CREATE OR REPLACE FUNCTION transaction_trigger()
  RETURNS TRIGGER AS
$my_trigger$
DECLARE 
  v_value             float;
BEGIN
  v_value := 0;
  raise notice 'id: %', NEW.id;
  raise notice 'value: %', v_value;
  SELECT balance.value INTO v_value FROM balance WHERE account_id = NEW.account_id;
  raise notice 'value: %', v_value;
  IF v_value is NULL THEN
    v_value := 0;
  END IF;
  IF NEW.type_of = 'credit' THEN
    v_value := v_value + NEW.value;
  ELSE
    v_value := v_value - NEW.value;
  END IF;
  raise notice 'value: %', v_value;
  INSERT INTO 
    balance (account_id, value) 
  VALUES (NEW.account_id, v_value) 
  ON CONFLICT 
    (account_id) 
  DO UPDATE SET 
    value = v_value;
  RETURN NULL;
END
$my_trigger$ LANGUAGE plpgsql;


CREATE TRIGGER transaction_insert AFTER insert
ON transaction
FOR EACH ROW EXECUTE FUNCTION transaction_trigger();
"""


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bc_identify', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bc_identify')
    )
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('id_gov', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bc_identify', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('current', 'saving', name='account_type'), nullable=False),
    sa.Column('person_owner', sa.Integer(), nullable=False),
    sa.Column('agency_owner', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agency_owner'], ['agency.id'], ),
    sa.ForeignKeyConstraint(['person_owner'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bc_identify')
    )
    op.create_table('balance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_of', sa.Enum('credit', 'charge', name='transaction_type'), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.execute(create_trigger)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('balance')
    op.drop_table('account')
    op.drop_table('person')
    op.drop_table('agency')
    # ### end Alembic commands ###