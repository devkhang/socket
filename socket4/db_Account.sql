create database socket_Account
go

use socket_Account
go

create table Account(
	username varchar(50),
	pwd varchar(50)
)
go

insert into Account (username,pwd)
values ('authaikhang','123456'),
('wibulord','0908'),
('a','1'),
('admin','123456')