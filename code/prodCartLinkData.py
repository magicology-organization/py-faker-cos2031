from faker import Faker

fake = Faker()

# Open a file for writing SQL queries
with open('prodCartLinkData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for cart_id in range(1, 8001):  # Assuming 8000 carts
        product_id = fake.random_int(min=1, max=20)  # Assuming 20 products
        quantity = fake.random_int(min=1, max=10)  # Adjust as needed

        insert_query = f"""
        INSERT INTO ProdCartLink (CartID, ProductID, Quantity)
        VALUES ({cart_id}, {product_id}, {quantity});
        """

        file.write(insert_query)
