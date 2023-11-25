from faker import Faker

fake = Faker()

with open('inventoryData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for product_id in range(1, 21):  # Assuming 20 products
        remaining_quantity = fake.random_int(
            min=50, max=100)  # Adjust as needed
        sold_quantity = fake.random_int(min=0, max=50)  # Adjust as needed

        insert_query = f"""
        INSERT INTO Inventory (ProductID, Remaining, SoldQuantity)
        VALUES ({product_id}, {remaining_quantity}, {sold_quantity});
        """

        file.write(insert_query)
