# http://requests.readthedocs.org/en/master/user/quickstart/#make-a-request
# post standard address tuples to es
# fields are LLID, TUPLE, LIVESTATUS, AOID, AOGUID, POSTALCODE, CODE, OKATO, OKTMO
#         integer,string,    integer, string ...
# fields are HOUSEGUID, AOGUID, POSTALCODE, FTSHBS
#            string, ...

import requests
import csv, json

#read tuples from csv
with open('fias.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        put_tuple_url = 'http://localhost:9200/stdaddr/stdtuples/' + row[0]
        #+ row[0]
        put_tuple_dat = {'TUPLE': row[1]}
        #print(put_tuple_url + put_tuple_dat )
        #indexing
        r = requests.post( put_tuple_url, data = json.dumps(put_tuple_dat) )
        #print(r.text)






