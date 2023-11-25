from faker import Faker
import random

fake = Faker()

# Open a file for writing SQL queries
with open('shipmentData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for shipment_id in range(1, 4326):  # Assuming 4325 shipments
        customer_id = random.randint(1, 8000)
        address = fake.address()
        status = fake.random_element(["Processing", "Shipped", "Delivered"])
        shipment_fee = fake.random.uniform(10, 200)  # Adjust as needed
        received_date = fake.date_this_year()

        insert_query = f"""
        INSERT INTO Shipment (CustomerID, Address, Status, ShipmentFee, ReceivedDate)
        VALUES ({customer_id}, "{address}", "{status}", {shipment_fee:.2f}, "{received_date}");
        """

        file.write(insert_query)
