'''
You may want to generate some new random sales data to check your extension code.

This will produce some - you can change the products or anything else below.

'''

import random
import faker
import pandas as pd

# Initialize the Faker instance to generate random data
fake = faker.Faker()

# Generate spoof sales data
sales_data = []
for _ in range(200):
    sales_data.append({
        'Order ID': fake.uuid4(),
        'Customer Name': fake.name(),
        'Product': random.choice(['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor', 'Keyboard']),
        'Quantity': random.randint(1, 5),
        'Unit Price': round(random.uniform(50, 1500), 2),
        'Total Sale': 0,  # Will calculate this below
        'Sale Date': fake.date_this_year()
    })

# Calculate Total Sale as Quantity * Unit Price
for record in sales_data:
    record['Total Sale'] = round(record['Quantity'] * record['Unit Price'], 2)

# Convert to a DataFrame
sales_df = pd.DataFrame(sales_data)


fout = input("Enter the filename you want: ")

# Save the spoof sales data to a CSV file
file_path_sales = fout
sales_df.to_csv(file_path_sales, index=False)

