create table CLIENT_MASTER(CLIENTNO Varchar(6), NAME Varchar(20),ADDRESS1 VARCHAR(30), ADDRESS2 varchar(30),CITY varchar(15),PINCODE numeric(8),STATE varchar(15),BALDUE DEC(10,0) );
select * from CLIENT_MASTER;
insert into CLIENT_MASTER Values('C00001','ivan bayroos','','','Mumbai','400054','Maharastra','15000');
insert into CLIENT_MASTER Values('C00002','Mamta Muzumdar','','','Madras','780001','Tamil Nadu','0');
insert into CLIENT_MASTER Values('C00003','Chhaya Bankar','','','Mumbai','400057','Maharastra','5000');
insert into CLIENT_MASTER Values('C00004','Ashwini Joshi','','','Banglore','560001','Karnataka','0');
insert into CLIENT_MASTER Values('C00005','Hansel colaco','','','Mumbai','400060','Maharastra','2000');
insert into CLIENT_MASTER Values('C00006','Deepak Sharma','','','Manglore','560050','Karnataka','0');


Select NAME from CLIENT_MASTER;

delete from CLIENT_MASTER ;
Select *from CLIENT_MASTER;

select NAME , CITY , STATE From CLIENT_MASTER;

Select NAME from CLIENT_MASTER Where CITY = 'Mumbai' 



drop table CLIENT_MASTER;

PRIMARY KEY TABLE
create table CLIENT_MASTER(CLIENTNO Varchar(6) primary key, NAME Varchar(20) Not null,ADDRESS1 VARCHAR(30), ADDRESS2 varchar(30),CITY varchar(15),PINCODE numeric(8),STATE varchar(15),BALDUE DEC(10,0) );
select * from CLIENT_MASTER;
insert into CLIENT_MASTER Values('C00001','ivan bayroos','','','Mumbai','400054','Maharastra','15000');
insert into CLIENT_MASTER Values('C00002','Mamta Muzumdar','','','Madras','780001','Tamil Nadu','0');
insert into CLIENT_MASTER Values('C00003','Chhaya Bankar','','','Mumbai','400057','Maharastra','5000');
insert into CLIENT_MASTER Values('C00004','Ashwini Joshi','','','Banglore','560001','Karnataka','0');
insert into CLIENT_MASTER Values('C00005','Hansel colaco','','','Mumbai','400060','Maharastra','2000');
insert into CLIENT_MASTER Values('C00006','Deepak Sharma','','','Manglore','560050','Karnataka','0');

insert into CLIENT_MASTER Values('C00001','ivan bayroos','address1','address2','Mumbai','400054','Maharastra','15000');
insert into CLIENT_MASTER Values('C00002','Mamta Muzumdar','address1','address2','Madras','780001','Tamil Nadu','0');
insert into CLIENT_MASTER Values('C00003','Chhaya Bankar','address1','address2','Mumbai','400057','Maharastra','5000');
insert into CLIENT_MASTER Values('C00004','Ashwini Joshi','address1','address2','Banglore','560001','Karnataka','0');
insert into CLIENT_MASTER Values('C00005','Hansel colaco','address1','address2','Mumbai','400060','Maharastra','2000');
insert into CLIENT_MASTER Values('C00006','Deepak Sharma','address1','address2','Manglore','560050','Karnataka','0');
