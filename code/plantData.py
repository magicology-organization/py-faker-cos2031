from faker import Faker
import random

fake = Faker()

# Open a file for writing SQL queries
with open('plantData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for plant_id in range(1, 2674):  # Assuming 2673 records
        field_id = random.randint(1, 100)  # Assuming 100 fields
        humidity = fake.random.uniform(40, 80)  # Adjust as needed
        temperature = fake.random.uniform(20, 30)  # Adjust as needed

        insert_query = f"""
        INSERT INTO Plant (FieldID, Humidity, Temp)
        VALUES ({field_id}, {humidity:.2f}, {temperature:.2f});
        """

        file.write(insert_query)
