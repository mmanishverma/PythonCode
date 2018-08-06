import pyodbc
import csv
out_file = "products.csv"
server = 'tcp:n8cn44tzr4.database.windows.net,1433'
database = 'itrackleaves'
username = 'cvadmin@n8cn44tzr4;'
password = 'P@ssw0rd'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=21443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("select * from product where id < 10000")
row = cursor.fetchone()
#f=open("prod.txt","w+")
writer = csv.writer(open("prod.csv", "wb"))
while row:
  print (str(row[0]) + "," + str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))
  myrow = (str(row[0]) + "," + str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))
  # writer.writerow(myrow)
  writer.writerow(str(row[0]) + "," + str(row[1].encode("utf-8","replace"))+ "," + str(row[2].encode("utf-8","replace")))
  row = cursor.fetchone()
  myrow = ""

#cursor1= cnxn.cursor()
#cursor1.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Product' ")
#row2 = cursor1.fetchone()
#while row2:
#  print (str(row2[0]) + " " + str(row2[1].encode("utf-8","replace"))+ " " + str(row2[2].encode("utf-8","replace")))
#  writer = csv.writer(open("out2.csv", "w"))
#  writer.writerows(str(row2[0])+" "+ str(row2[1].encode("utf-8","replace"))+ " "+ str(row2[2].encode("utf-8","replace"))
#  row2 = cursor1.fetchone()
