DECLARE
    date1 DATE := TO_DATE('&new_dt', 'DD-MON-YYYY');
    day VARCHAR2(15);
    BEGIN
    day := RTRIM(TO_CHAR(date1, 'DAY'));
    IF day IN ('SATURDAY', 'SUNDAY') THEN
    dbms_output.new_line;
    DBMS_OUTPUT.PUT_LINE 
    ('The day of the given date is '||day||' and it falls on weekend');
    ELSE
    dbms_output.new_line;
    DBMS_OUTPUT.PUT_LINE ('The day of the given date is '||day||' and it does not fall on the weekend');
    END IF;
    DBMS_OUTPUT.PUT_LINE ('Execution  Successful');
END;