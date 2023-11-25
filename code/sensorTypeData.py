from faker import Faker
import random

fake = Faker()

# Open a file for writing SQL queries
with open('sensorTypeData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for _ in range(437):  # Assuming 437 rows
        provider_id = random.randint(1, 100)
        cost = fake.random.uniform(100, 1000)  # Adjust cost range as needed
        installed = fake.boolean()
        reserved = fake.boolean()

        insert_query = f"""
        INSERT INTO SensorType (ProviderID, Cost, Installed, Reserved)
        VALUES ({provider_id}, {cost:.2f}, {installed}, {reserved});
        """

        file.write(insert_query)
