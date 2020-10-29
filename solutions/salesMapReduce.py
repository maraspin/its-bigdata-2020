from functools import reduce
import json

with open('../samples/sales.json', 'r') as f:
    sales_data = json.load(f)

country_record = (list(map(lambda record: (str(record["year"]) + "-" + str(record["month"]), record["value"]), sales_data)))
#print(country_record)

country_result = reduce(lambda val1, val2: val1 + val2, sorted(country_record))
print(country_result)

