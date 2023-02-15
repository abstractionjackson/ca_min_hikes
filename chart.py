import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def main():
    # path: data/minwagehist.json
    # Load the JSON data into a Python data structure
    with open('data/minwagehist.json') as f:
        data = json.load(f)

    # Extract the timestamps and values from the data structure
    dates = data['date']
    wages = data['wage']

    # Convert the timestamps to datetime objects
    dates = [datetime.fromisoformat(date) for date in dates]

    # Create a plot using Matplotlib
    fig, ax = plt.subplots()
    ax.plot(dates, wages)

    # Set the x-axis label to 'Time' and the y-axis label to 'Value'
    ax.set_xlabel('Date')
    ax.set_ylabel('Wage (USD)')

    # Set the plot title
    ax.set_title('Minimum Wage, California')

    # Format the y-axis to display currency
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
