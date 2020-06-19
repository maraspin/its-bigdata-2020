#!/bin/sh

if [ $# -eq 0 ]; then
  echo "Usage $0 INDEX [N] (not to execute mapping)"
  exit 1
fi

INDEX=$1

python3 ./convert.py account-data.json
curl -H "Content-Type: application/json" -XDELETE "bigdata.its:9200/${INDEX}"

if [ $# -eq 1 ]; then
  echo "Adding Mapping"
  curl -H "Content-Type: application/json" -XPUT "bigdata.its:9200/${INDEX}" --data-binary "@analyzer.json"
  curl -H "Content-Type: application/json" -XPUT "bigdata.its:9200/${INDEX}/_mapping" --data-binary "@mapping.json"
fi

echo "Bulk Indexing"
curl -H "Content-Type: application/json" -XPOST "bigdata.its:9200/${INDEX}/_bulk?pretty&refresh" --data-binary "@es-account-data.json"
