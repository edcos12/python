import csv

companies = []
sales = []
yearly_sales = []

with open("D:\\Users\\edward\\codes\\Python\\lessons\\file\\carSales.csv", newline = "") as file:
    reader = csv.reader(file, delimiter=",")
    next(reader)
    for row in reader:
        companies.append(row[0])
        sales.append([int(x.replace(",", "")) for x in row[1:]])

    for i in range(len(companies)):
        total = sum(sales[i])
        yearly_sales.append(total)
        print("{} monthly sales: {}, Total yearly sales = {}".format(companies[i], sales[i], yearly_sales[i]))
    
    

