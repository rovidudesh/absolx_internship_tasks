def load_sales_data(file_path="sales_data.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
