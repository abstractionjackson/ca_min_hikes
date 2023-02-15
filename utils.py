def isHeader(row, header_key="header"):
    try:
        return header_key in row['class']
    except KeyError:
        return False
def getHeaders(table):
    return [
       value.text for value in table.find_all('th')
    ]
def getData(row):
    return [
        value.text for value in row.find_all('td')
    ]
def getRows(table, header_key="header"):
   return [
        getData(row) for row in table.find_all('tr') if not isHeader(row, header_key) 
    ]
def mapTableToDict(table, header_key="header"):
    headers = getHeaders(table)
    rows = getRows(table, header_key)
    return {
        headers[i]: [
            row[i] for row in rows
        ] for i in range(len(headers))
    }
def parseWage(wage):
    # wage: string "$7.25/hour"
    # return: float 7.25
    return float(wage.split("/")[0].replace("$",""))
