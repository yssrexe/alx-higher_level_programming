-- Write a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE if NOT EXISTS cities(
    id INT unique AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(state_id)
);
