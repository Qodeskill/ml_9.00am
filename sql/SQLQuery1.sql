--create table student(fname varchar(10),lname varchar(10),course varchar(10));
--insert into student values('Nirbhay','Kotadiya','Nodejs');
--insert into student values('Ashish','Dhola','Nodejs');
--insert into student values('Nirav','Mungala','C++');
--insert into student values('Umang','Mordiya','Nodejs');
--select * from student;
--select fname,course from student;

--create table student1(rollno int not null primary key, fname varchar(10) , lname varchar(10),course varchar(10));
--drop table student1
insert into student1 values(1,'Nirbhay','Kotadiya','Nodejs');
insert into student1 values(2,'Ashish','Dhola','Nodejs');
insert into student1 values(3,'Nirav','Mungala','C++');
insert into student1 values(4,'Umang','Mordiya','Nodejs');

select * from student

ALTER TABLE student 
ADD CONSTRAINT pk_StudentID notnull (sid)  

--create table location(add_id int not null primary key,rollno int references student, landmark varchar(25) , address1 varchar(25),address2 varchar(25));

insert into location values(1,1,'khatodara','Someshwar soc','surat');
select * from location 