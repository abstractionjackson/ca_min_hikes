import json
from bs4 import BeautifulSoup
from dateutil.parser import parse
from .utils import *

# read the html file
path = 'data/minwagehist.html'

def main():
    with open(path) as f:
        soup = BeautifulSoup(f, 'html.parser')
        # get the tables
        tables = soup.find_all('table')
        # header key = "column_labels"
        header_key = 'column_labels'
        # for each table, 
        # map the headers to keys, the rows to values
        data = [mapTableToDict(table,header_key) for table in tables]
        # combine the two tables
        # the first table splits wage data into separate columns
        # based on the size of the companies. Our application is concerned
        # with large companies, under the key "26 Employees or More"
        # so, prepend the dates, and the amounts from the first table to the second
        date_key = "date"
        wage_key = "wage"
        table_1 = data[0]
        table_2 = data[1]
        table_1_date_key=(next((key for key in table_1 if "Date" in key), None))
        table_1_wage_key=(next((key for key in table_1 if "26 Employees or More" in key), None))
        table_2_date_key = table_1_date_key
        table_2_wage_key = next((key for key in table_2 if "Minimum Wage" in key), None)
        print(f"Mapping {date_key} <-- {table_1_date_key} + {table_2_date_key} \nMapping {wage_key} <-- {table_1_wage_key} + {table_2_wage_key}")
        
        data = {
            "date": [],
            "wage": []
        }
       
        for row in table_1[table_1_date_key]:
            data[date_key].append(parse(row).strftime("%Y-%m-%d"))
        for row in table_1[table_1_wage_key]:
            data[wage_key].append(parseWage(row))
        for row in table_2[table_2_date_key]:
            data[date_key].append(parse(row).strftime("%Y-%m-%d"))
        for row in table_2[table_2_wage_key]:
            data[wage_key].append(parseWage(row))

        # write the data to a json file
        with open('data/minwagehist.json', 'w') as f:
            json.dump(data, f)
        print('Done')

if __name__ == "__main__":
    main()
