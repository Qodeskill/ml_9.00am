select CLIENT_MASTER.NAME
	,CLIENT_MASTER.CLIENTNO
	,SALES_ORDER.ORDERNO
	,SALES_ORDER_DETAILS.PRODUCTNO
	,PRODUCT_MASTER.DESCRIPTION
from CLIENT_MASTER
inner join SALES_ORDER on CLIENT_MASTER.CLIENTNO = SALES_ORDER.CLIENTNO
inner join SALES_ORDER_DETAILS on SALES_ORDER.ORDERNO = SALES_ORDER_DETAILS.ORDERNO
inner join PRODUCT_MASTER on SALES_ORDER_DETAILS.PRODUCTNO = PRODUCT_MASTER.PRODUCTNO
where CLIENT_MASTER.CLIENTNO='C00001'

SELECT
    *
FROM
    sales.orders o
WHERE
    EXISTS (
        SELECT
            customer_id
        FROM
            sales.customers c
        WHERE
            o.customer_id = c.customer_id
        AND city = 'San Jose'
    )
ORDER BY
    o.customer_id,
    order_date;

select description,SELLPRICE from PRODUCT_MASTER
where EXISTS(
select productno from SALES_ORDER_DETAILS
where exists (
select orderno from SALES_ORDER  
where salesmanno  in (
select SALESMANNO from SALESMAN_MASTER
where SALESMANNO = 'S00001'
)))