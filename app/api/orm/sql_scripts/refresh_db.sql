-- USE FOR TESTING ONLY
-- DELETE ALL THE ROWS FROM ALL THE TABLES.
-- EMPTY THE DB TO SET IT READY FOR TESTS.

DO $$
DECLARE
    v_table_name text;
BEGIN
    FOR v_table_name IN (SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE')
    LOOP
        IF v_table_name <> 'alembic_version' THEN
            EXECUTE 'DELETE FROM ' || v_table_name || ' CASCADE;';
        END IF;
    END LOOP;
END $$;
