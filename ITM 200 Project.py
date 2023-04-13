import csv
import matplotlib.pyplot as plt


with open('data.csv', 'r') as read:
   csv_reader = csv.reader(read)
   lines = next(csv_reader)
   sales_data = list(csv_reader)

sales = []
years = []
for i in range(len(sales_data)):
   year_sales = sum([int(sales_data[i][j]) for j in range(1, len(lines))])
   sales.append(year_sales)
   years.append(int(sales_data[i][0]))

sales_2021 = [int(sales_data[9][i]) for i in range(1, 7)]
sales_2022 = []
for i in range(1, 7):
   try:
       sales_2022.append(int(sales_data[10][i]))
   except:
       sales_2022.append(0)

Sales2021 = sum(sales_2021)
Sales2022 = sum(sales_2022)
SGR = (Sales2022 - Sales2021) / Sales2022

sales_2022_estimated = []
for i in range(7, 13):
   sales_2022_estimated.append(int(sales_data[9][i]) + int(sales_data[9][i]) * SGR)

months = lines[1:]
months_2022 = [f"{m} 2022" for m in months[6:]]
plt.barh(months_2022, sales_2022_estimated)
plt.xlabel('Estimated Sales')
plt.title('Estimated Sales for Last 6 Months of 2022')
plt.show()

with open('stats.txt', mode='w') as read:
    for i in range(len(sales)):
        read.write(f"{years[i]}: {sales[i]}\n")

    read.write(f"First 6 months of 2021: {Sales2021}\n")
    read.write(f"Last 6 months of 2022: {Sales2022}\n")

    read.write(f"Sales Growth Rate: {SGR:.2%}\n")

    read.write("Estimated Sales for Last 6 Months of 2022:\n")
    for i in range(6):
        read.write(f"{months_2022[i]}: {sales_2022_estimated[i]:.0f}\n")

plt.bar(years, sales)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Total Sales per Year')
plt.show()

sales_2022_estimated = []
for i in range(7, 13):
   sales_2022_estimated.append(int(sales_data[9][i]) + int(sales_data[9][i]) * SGR)
