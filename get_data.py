import requests as r

url = 'https://www.dir.ca.gov/iwc/minimumwagehistory.htm'

# request the page, save the result to /data
# and print the status code

def get_page(url):
    page = r.get(url)
    print(page.status_code)
    return page

def write_page(page):
    with open('data/minwagehist.html', 'w') as f:
        f.write(page.text)

def main():
    page = get_page(url)
    write_page(page)

if __name__ == '__main__':
    main()
