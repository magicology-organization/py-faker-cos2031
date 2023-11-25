from faker import Faker

fake = Faker()

# Open a file for writing SQL queries
with open('fieldData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for _ in range(100):  # Assuming 100 fields
        field_size = fake.random_element(["Small", "Medium", "Large"])
        field_type = fake.random_element(
            ["Wheat", "Corn", "Rice", "Soybeans", "Other"])
        date_planted = fake.date()

        insert_query = f"""
        INSERT INTO Field (FieldSize, FieldType, DatePlanted)
        VALUES ("{field_size}", "{field_type}", "{date_planted}");
        """

        file.write(insert_query)
