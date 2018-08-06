import pyodbc
import csv
out_file = "products.csv"
server = '180.179.50.82,21443'
database = 'LuxeIndia'
username = 'radia'
password = 'Lx@20#9~17'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=21443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("select * from product")
data = cursor.fetchall()

with open('prodnew.csv', 'w') as f_handle:
    writer = csv.writer(f_handle)
    # Add the header/column names
    header = ['id', 'name', 'short desc']
    writer.writerow(header)
    # Iterate over `data`  and  write to the csv file
    for row in data:
        writer.writerow(row)
        print (str(row[0]) + "," + str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))
    #myrow = (str(row[0]) + "," + str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))


