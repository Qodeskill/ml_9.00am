create table SALES_ORDER_DETAILS (
	ORDERNO varchar(6) references SALES_ORDER 
	,PRODUCTNO varchar(6) references PRODUCT_MASTER 
	,QTYORDERD numeric(8)
	,QTYDISP numeric(8)
	,PRODUCTRATE decimal(10, 2)
	);

insert into SALES_ORDER_DETAILS values('019001','P00001','4','4','525')
insert into SALES_ORDER_DETAILS values('019001','P00003','2','1','8400');
insert into SALES_ORDER_DETAILS values('019001','P00002','2','1','5250');
insert into SALES_ORDER_DETAILS values('019002','P00001','10','0','525');
insert into SALES_ORDER_DETAILS values('046865','P00002','3','3','3150');
insert into SALES_ORDER_DETAILS values('046865','P00009','3','1','5250');
insert into SALES_ORDER_DETAILS values('046865','P00003','10','10','525');
insert into SALES_ORDER_DETAILS values('046865','P00004','4','4','1050');
insert into SALES_ORDER_DETAILS values('019003','P00005','2','2','1050');
insert into SALES_ORDER_DETAILS values('019003','P00006','1','1','12000');
insert into SALES_ORDER_DETAILS values('046866','P00003','1','0','8400');
insert into SALES_ORDER_DETAILS values('046866','P00008','1','0','1050');
insert into SALES_ORDER_DETAILS values('019008','P00001','10','5','525');
insert into SALES_ORDER_DETAILS values('019008','P00007','5','3','1050');