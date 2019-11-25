import adClient
import csv

with open('sample.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        username = row['username']
        employee_id = row['employee_id']
        official_name = row['official_name']
        print(username, employee_id, official_name)
        # adClient.create_user(username, employee_id, official_name, active=True)
        adClient.manage_user(username, mode='delete')
