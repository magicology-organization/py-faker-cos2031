from faker import Faker

fake = Faker()

# Open a file for writing SQL queries
with open('reviewData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for _ in range(2435):  # Assuming 1000 reviews
        product_id = fake.random_int(min=1, max=20)  # Assuming 20 products
        customer_name = fake.name()
        content = fake.paragraph()
        rating = fake.random_int(min=1, max=5)

        insert_query = f"""
        INSERT INTO Review (ProductID, CustomerName, Content, Rating)
        VALUES ({product_id}, "{customer_name}", "{content}", {rating});
        """

        file.write(insert_query)
