from faker import Faker

fake = Faker()

# Open a file for writing SQL queries
with open('providerData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for _ in range(100):  # Assuming 100 providers
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()
        name = fake.company()

        insert_query = f"""
        INSERT INTO Provider (Address, Phone, Email, Name)
        VALUES ("{address}", "{phone}", "{email}", "{name}");
        """

        file.write(insert_query)
