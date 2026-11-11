show databases;
create database blood_db_aug26;
use blood_db_aug26;
create table Donor(id int primary key auto_increment,
name varchar(100),
blood_group varchar(5),
phone varchar(15) unique,
city varchar(100),
last_donation date
)
select * from Donor;
use blood_db_aug26;
select * from Donor;
select * from DONOR;
select * from donor;
