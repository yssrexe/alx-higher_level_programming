--  script that creates the table unique_id
CREATE TABLE if NOT EXISTS unique_id(
    id INT default 1 unique,
    name VARCHAR(256)
);