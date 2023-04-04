CREATE DATABASE laundry;

USE laundry;

CREATE TABLE orders (
    order_id real, 
    client_email varchar(30), 
    order_amount real,
    order_entered DATETIME DEFAULT CURRENT_TIMESTAMP, 
    stage_finished_at DATETIME, 
    stage ENUM('entered','washed','delivered') DEFAULT 'entered',
    order_notes varchar(40)
);

CREATE TABLE clients (
    name VARCHAR(30), 
    family_name VARCHAR(30), 
    city VARCHAR(30),
    street VARCHAR(30),
    house_number real,
    phone VARCHAR(30), 
    client_email VARCHAR(30),
    message_type ENUM('email','sms','None')
);

CREATE TABLE equipment (
    equipment_name VARCHAR(30) PRIMARY KEY,
    equipment_value NUMERIC(10,0)
);

CREATE TABLE variables (
    variable_name VARCHAR(30) PRIMARY KEY,
    variable_value NUMERIC(10,2)
);