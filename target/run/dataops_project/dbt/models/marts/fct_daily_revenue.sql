
  
    
    

    create  table
      "warehouse"."main"."fct_daily_revenue__dbt_tmp"
  
    as (
      with sales as (
    select * from "warehouse"."main"."stg_sales"
),

daily_revenue as (
    select
       cast(InvoiceDate as date) as sale_date,
        sum(Quantity * UnitPrice) as daily_revenue
    from sales
    group by 1
)

select * from daily_revenue
    );
  
  