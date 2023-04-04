CREATE DATABASE laundry;

USE laundry;

CREATE TABLE orders (
    order_id varchar(30), 
    client_id varchar(30), 
    order_type varchar(30),
    order_amount real, 
    order_entered DATETIME DEFAULT CURRENT_TIMESTAMP, 
    stage_finished_at DATETIME, 
    stage ENUM('entered','washed','delivered') 
);

CREATE TABLE clients (
    name VARCHAR(30), 
    family_name VARCHAR(30), 
    city VARCHAR(30), 
    address VARCHAR(30), 
    address_number VARCHAR(30), 
    home_phone VARCHAR(30), 
    phone_1 VARCHAR(30), 
    phone_2 VARCHAR(30), 
    client_id VARCHAR(30), 
    e_mail VARCHAR(30), 
    message_type ENUM('mail','text','None')    
);

