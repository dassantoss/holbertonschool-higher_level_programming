-- Advanced Task: Convert hbtn_0c_0 database, first_table table, and name field to UTF8 (utf8mb4) with collate utf8mb4_unicode_ci.

USE hbtn_0c_0;

-- Convert the hbtn_0c_0 database to UTF8 with collate utf8mb4_unicode_ci.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the first_table table to UTF8 with collate utf8mb4_unicode_ci.
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in the first_table table to UTF8 with collate utf8mb4_unicode_ci.
ALTER TABLE first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
