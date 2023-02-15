# if main.py is in a package, then __init__.py must be present
from . import get_data
from . import parse_tables
from . import chart

def main():
    get_data()
    parse_tables()
    chart()

if __name__ == "__main__":
    main()
