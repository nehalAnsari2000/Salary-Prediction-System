import csv
import random

# Function to generate synthetic salary data
def generate_salary_data(num_records):
    data = []
    for _ in range(num_records):
        years_of_experience = round(random.uniform(1, 30), 1)  # Random experience between 1 and 30 years
        base_salary = 30500 + (years_of_experience * 9000)  # Base salary increases with experience
        salary = base_salary + random.uniform(-5000, 5000)  # Add some randomness
        salary = max(30500, min(300000, salary))  # Ensure salary stays within the specified range
        data.append([years_of_experience, round(salary)])
    return data

# Save data to CSV file
def save_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Years of Experience', 'Salary'])  # Write header
        writer.writerows(data)  # Write data rows

# Generate 500 records
num_records = 500
salary_data = generate_salary_data(num_records)

# Save to CSV file
csv_filename = 'salary_large.csv'
save_to_csv(csv_filename, salary_data)

print(f"Generated {num_records} records and saved to '{csv_filename}'.")