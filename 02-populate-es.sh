#!/bin/bash

# We make sure no index named visualization already exists
/usr/bin/curl -H "Content-Type: application/json" -XDELETE 'bigdata.its:9200/visualization'

# We do use bulk insert to add contents of file samples/es-account-data.json into visualization index
/usr/bin/curl -H "Content-Type: application/json" -XPOST 'bigdata.its:9200/visualization/_bulk?pretty&refresh' --data-binary "@samples/es-account-data.json"
