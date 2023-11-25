from faker import Faker
import random

fake = Faker()

# Open a file for writing SQL queries
with open('invoiceData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for invoice_id in range(1, 4326):  # Assuming 4325 invoices
        cart_id = random.randint(1, 7000)
        customer_id = random.randint(1, 8000)
        payment_method = fake.random_element(
            ["Credit Card", "PayPal", "Bank Transfer"])
        payment_status = fake.random_element(["Pending", "Paid", "Failed"])
        # Assuming each invoice is linked to a shipment with the same ID
        shipment_id = invoice_id
        invoice_date = fake.date_this_year()

        insert_query = f"""
        INSERT INTO Invoice (CartID, CustomerID, PaymentMethod, PaymentStatus, ShipmentID, InvoiceDate)
        VALUES ({cart_id}, {customer_id}, "{payment_method}", "{payment_status}", {shipment_id}, "{invoice_date}");
        """

        file.write(insert_query)
