from faker import Faker
import random

fake = Faker()

# Open a file for writing SQL queries
with open('sensorData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for sensor_id in range(1, 1235):  # Assuming 5000 sensors
        field_id = random.randint(1, 100)
        sensor_type_id = random.randint(1, 437)
        employee_id = random.randint(60, 740)
        status = fake.random_element(["Active", "Inactive"])
        install_date = fake.date_this_decade()
        last_updated = fake.date_time_this_month()

        insert_query = f"""
        INSERT INTO Sensor (FieldID, SensorTypeID, EmployeeID, Status, InstallDate, LastUpdated)
        VALUES ({field_id}, {sensor_type_id}, {employee_id}, "{status}", "{install_date}", "{last_updated}");
        """

        file.write(insert_query)
