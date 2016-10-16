# http://requests.readthedocs.org/en/master/user/quickstart/#make-a-request
# post standard address full addition data to es
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
        put_full_url = 'http://localhost:9200/stdaddr/stdfull/' + row[0]
        #LLID -> row[0] _id
        put_full_dat = {'LIVESTATUS': row[2], 'AOID': row[3], 'AOGUID': row[4], 'POSTALCODE': row[5], 'CODE': row[6], 'OKATO': row[7], 'OKTMO': row[8]}
        #print(put_tuple_url + put_tuple_dat )
        #indexing
        r = requests.post( put_full_url, data = json.dumps(put_full_dat) )
        #print(r.text)






