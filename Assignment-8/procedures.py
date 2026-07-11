CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_username VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM phonebook
        WHERE username = p_username
    ) THEN

        UPDATE phonebook
        SET phone = p_phone
        WHERE username = p_username;

    ELSE

        INSERT INTO phonebook(username, phone)
        VALUES(p_username, p_phone);

    END IF;
END;
$$;
