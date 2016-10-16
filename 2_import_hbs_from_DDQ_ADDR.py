#http://mkleehammer.github.io/pyodbc/
import pyodbc, csv

#connect to database
cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=localhost; DATABASE=DDQ_ADDR')
cursor = cnxn.cursor()

#SQL-query
cursor.execute("select HOUSEGUID, AOGUID, POSTALCODE, FTSHBS from FTSHBS")

#fetch data
rows = cursor.fetchall()

#lookup
#for row in rows:
#    print(row.HOUSEGUID, row.AOGUID, row.POSTALCODE, row.FTSHBS)

#export CSV
with open('fias_hbs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow([row.HOUSEGUID, row.AOGUID, row.POSTALCODE, row.FTSHBS])

