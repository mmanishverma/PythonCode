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
row = cursor.fetchone()
writer = csv.writer(open("prod.csv", "wb"))
while row:
  print (str(row[0]) + "," + str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))
#  myrow = (str(row[0]) + "," + str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))
  writer.writerow(str(row[0]+" , "+str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))
# writer.writerow(str(row[0]) + "," + str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))
  row = cursor.fetchone()
cursor1 = cnxn.cursor()

                  
cursor1.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Product' ")
row2 = cursor1.fetchone()
while row2:
  print (str(row2[0]) + " " + str(row2[1].encode("utf-8","replace"))+ " " + str(row2[2].encode("utf-8","replace")))
  writer = csv.writer(open("out2.csv", "w"))
  writer.writerows(str(row2[0])+" "+ str(row2[1].encode("utf-8","replace"))+ " "+ str(row2[2].encode("utf-8","replace"))
  row2 = cursor1.fetchone()
