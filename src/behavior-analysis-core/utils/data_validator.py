def validate_columns(data) -> bool:
    columns = data.columns
    columns_names = ["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID",
                     "Country"]
    for column_name in columns_names:
        if column_name not in columns:
            return False

    return True
