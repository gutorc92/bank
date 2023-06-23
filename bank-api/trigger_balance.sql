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

INSERT INTO transaction (type_of, date, value, account_id) VALUES ('credit', '2023-06-06', 100, 1);