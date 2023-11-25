from faker import Faker

fake = Faker()

# Open a file for writing SQL queries
with open('productFieldData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    # Assuming 20 products and 100 fields
    for product_field_id in range(1, 101):
        product_id = fake.random_int(min=1, max=20)
        field_id = fake.random_int(min=1, max=100)

        insert_query = f"""
        INSERT INTO ProductField (ProductID, FieldID)
        VALUES ({product_id}, {field_id});
        """

        file.write(insert_query)
