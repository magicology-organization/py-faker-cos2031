# Open a file for writing SQL queries
with open('cartData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for customer_id in range(1, 8001):  # Assuming 8000 customers
        insert_query = f"""
        INSERT INTO Cart (CustomerID)
        VALUES ({customer_id});
        """

        file.write(insert_query)
