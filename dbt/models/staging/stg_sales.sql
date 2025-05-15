with source as (
    select
        InvoiceNo,
        StockCode,
        Description,
        Quantity,
        InvoiceDate,
        UnitPrice,
        CustomerID,
        Country
    from read_csv_auto('/workspaces/dataops/data/sales.csv')
),

cleaned as (
    select
        cast(InvoiceNo as varchar) as InvoiceNo,
        cast(StockCode as varchar) as StockCode,
        Description,
        cast(Quantity as integer) as Quantity,
        cast(InvoiceDate as timestamp) as InvoiceDate,
        cast(UnitPrice as double) as UnitPrice,
        cast(CustomerID as varchar) as CustomerID,
        Country
    from source
    where CustomerID is not null
      and UnitPrice is not null
)

select * from cleaned
