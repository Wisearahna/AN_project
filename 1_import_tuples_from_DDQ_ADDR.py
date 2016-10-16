#http://mkleehammer.github.io/pyodbc/
import pyodbc, csv

#connect to database
cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=localhost; DATABASE=DDQ_ADDR')
cursor = cnxn.cursor()

#SQL-query
cursor.execute("select LLID, TUPLE, LIVESTATUS, AOID, AOGUID, POSTALCODE, CODE, OKATO, OKTMO from RECOVERYLINKSFULL")

#fetch data
rows = cursor.fetchall()

#lookup
#for row in rows:
#    print(row.LLID, row.TUPLE, row.LIVESTATUS, row.AOID, row.AOGUID, row.POSTALCODE, row.CODE, row.OKATO, row.OKTMO)

#export CSV
with open('fias.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow([row.LLID, row.TUPLE, row.LIVESTATUS, row.AOID, row.AOGUID, row.POSTALCODE, row.CODE, row.OKATO, row.OKTMO])
