# http://requests.readthedocs.org/en/master/user/quickstart/#make-a-request
# post standard address hbs data to es
# fields are LLID, TUPLE, LIVESTATUS, AOID, AOGUID, POSTALCODE, CODE, OKATO, OKTMO
#         integer,string,    integer, string ...
# fields are HOUSEGUID, AOGUID, POSTALCODE, FTSHBS
#            string, ...

import requests
import csv, json

#read tuples from csv
with open('fias_hbs.csv') as f:
    reader = csv.reader(f)
    id = 1
    for row in reader:
        put_hbs_url = 'http://localhost:9200/stdaddr/stdhbs/' + str(id)
        #make integer id of record
        id=id+1
        put_hbs_dat = {'HOUSEGUID': row[0], 'AOGUID': row[1], 'POSTALCODE': row[2].strip(), 'FTSHBS': row[3].lstrip()}
        #print(put_tuple_url + put_tuple_dat )
        #indexing
        r = requests.post( put_hbs_url, data = json.dumps(put_hbs_dat) )
        #print(r.text)






