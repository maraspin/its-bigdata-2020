#!/bin/bash

INDEXNAME=visualize

# We make sure no index named visualization already exists
/usr/bin/curl -H "Content-Type: application/json" -XDELETE 'bigdata.its:9200/'$INDEXNAME

# We do create a mapping for our new index visualize
/usr/bin/curl -XPUT 'bigdata.its:9200/'$INDEXNAME
/usr/bin/curl -H "Content-Type: application/json" -XPUT 'bigdata.its:9200/'$INDEXNAME'/_mapping' --data-binary "@samples/es-account-mapping.json"

# We do use bulk insert to add contents of file samples/es-account-data.json into visualization index
/usr/bin/curl -H "Content-Type: application/json" -XPOST 'bigdata.its:9200/'$INDEXNAME'/_bulk?pretty&refresh' --data-binary "@samples/es-account-data.json"
