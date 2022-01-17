create table SALES_ORDER_DETAILS (
	ORDERNO varchar(6) references SALES_ORDER 
	,PRODUCTNO varchar(6) references PRODUCT_MASTER 
	,QTYORDERD numeric(8)
	,QTYDISP numeric(8)
	,PRODUCTRATE decimal(10, 2)
	);

insert into SALES_ORDER_DETAILS values('019001','P00001','4','4','525')
insert into SALES_ORDER_DETAILS values('019001','P07965','2','1','8400');
insert into SALES_ORDER_DETAILS values('019001','P07885','2','1','5250');
insert into SALES_ORDER_DETAILS values('019002','P00001','10','0','525');
insert into SALES_ORDER_DETAILS values('046865','P07868','3','3','3150');
insert into SALES_ORDER_DETAILS values('046865','P07885','3','1','5250');
insert into SALES_ORDER_DETAILS values('046865','P00001','10','10','525');
insert into SALES_ORDER_DETAILS values('046865','P0345','4','4','1050');
insert into SALES_ORDER_DETAILS values('019003','P03453','2','2','1050');
insert into SALES_ORDER_DETAILS values('019003','P06734','1','1','12000');
insert into SALES_ORDER_DETAILS values('046866','P07965','1','0','8400');
insert into SALES_ORDER_DETAILS values('046866','P07975','1','0','1050');
insert into SALES_ORDER_DETAILS values('019008','P00001','10','5','525');
insert into SALES_ORDER_DETAILS values('019008','P07975','5','3','1050');