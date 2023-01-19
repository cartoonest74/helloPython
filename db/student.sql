PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE student(
id integer primary key autoincrement not null,
name text not null default 'aaa',
mobile text null);
INSERT INTO student VALUES(1,'GD','010-1234-5678');
INSERT INTO student VALUES(2,'Top','010-0000-9999');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('student',2);
COMMIT;
