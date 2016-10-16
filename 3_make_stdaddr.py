#http://requests.readthedocs.org/en/master/user/quickstart/#make-a-request
# post standard address tuples to es
# fields are LLID, TUPLE, LIVESTATUS, AOID, AOGUID, POSTALCODE, CODE, OKATO, OKTMO
#         integer,string,    integer, string ...
# fields are HOUSEGUID, AOGUID, POSTALCODE, FTSHBS
#            string, ...

import requests as rest

#initial index
"""
//del
DELETE stdaddr

//create and mappings
PUT /stdaddr/
{
     "settings" : {
        "index" : {
            "number_of_shards" : 1,
            "number_of_replicas" : 1
        }
    },
 
  "mappings":{
    
    "stdtuples":{
      "properties":{
        "TUPLE":      { "type": "string" }
      }
    },
    
    "stdfull":{
      "properties":{
        "LIVESTATUS": { "type": "integer", "index": "not_analyzed" },
        "AOID":       { "type": "string",  "index": "not_analyzed" },
        "AOGUID":     { "type": "string",  "index": "not_analyzed" },
        "POSTALCODE": { "type": "string",  "index": "not_analyzed" },
        "CODE":       { "type": "string",  "index": "not_analyzed" },
        "OKATO":      { "type": "string",  "index": "not_analyzed" },
        "OKTMO":      { "type": "string",  "index": "not_analyzed" }
      }
    },
    
    "stdhbs":{
      "properties":{
        "HOUSEGUID":  { "type": "string",  "index": "not_analyzed" },
        "AOGUID":     { "type": "string",  "index": "not_analyzed" },
        "POSTALCODE": { "type": "string",  "index": "not_analyzed" },
        "HBS":        { "type": "string" }
        
      }
    }
    
  }
}
"""

#del
r = rest.delete('http://localhost:9200/stdaddr')
print(r.text)

put_create='{ "settings" : { "index" : { "number_of_shards" : 1, "number_of_replicas" : 1 } }, "mappings":{ "stdtuples":{ "properties":{ "TUPLE": { "type": "string" } } }, "stdfull":{ "properties":{ "LIVESTATUS": { "type": "integer", "index": "not_analyzed" }, "AOID": { "type": "string", "index": "not_analyzed" }, "AOGUID": { "type": "string", "index": "not_analyzed" }, "POSTALCODE": { "type": "string", "index": "not_analyzed" }, "CODE": { "type": "string", "index": "not_analyzed" }, "OKATO": { "type": "string", "index": "not_analyzed" }, "OKTMO":{ "type": "string",  "index": "not_analyzed" } } }, "stdhbs":{ "properties":{ "HOUSEGUID": { "type": "string", "index": "not_analyzed" }, "AOGUID": { "type": "string", "index": "not_analyzed" }, "POSTALCODE": { "type": "string", "index": "not_analyzed" }, "HBS": { "type": "string" } } } } }'

#create, mapping
r = rest.put('http://localhost:9200/stdaddr', data=put_create)
#print(r.text)






