from faker import Faker
import random

fake = Faker()

# Open a file for writing SQL queries
with open('helpData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for help_id in range(1, 2674):  # Assuming 1000 records
        customer_id = random.randint(1, 1000)  # Assuming 1000 customer records

        content = fake.text()
        employee_id = random.randint(100, 500)  # Assuming 100 employee records
        date = fake.date()
        status = fake.word()

        insert_query = f"""
        INSERT INTO Help (CustomerID, Content, EmployeeID, Date, Status)
        VALUES ({customer_id}, "{content}", {employee_id}, "{date}", "{status}");
        """

        file.write(insert_query)
