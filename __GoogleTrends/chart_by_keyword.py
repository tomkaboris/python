import warnings
import datetime
warnings.simplefilter(action='ignore', category=FutureWarning)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pytrends.request import TrendReq
import matplotlib.dates as mdates  # For date formatting

def get_keyword_trends(keyword):
    try:
        # Connect to Google
        pytrends = TrendReq(hl='en-US', tz=360)

        # Get the current date
        current_date = datetime.datetime.now()

        # Calculate date for 12 months ago
        last_year_date = current_date - datetime.timedelta(days=365)

        # Format dates in the required 'YYYY-MM-DD' format
        current_date_str = current_date.strftime('%Y-%m-%d')
        last_year_date_str = last_year_date.strftime('%Y-%m-%d')

        # Build payload for the last 12 months
        pytrends.build_payload([keyword], cat=0, timeframe=f'{last_year_date_str} {current_date_str}', geo='RS', gprop='')
        data_last_12_months = pytrends.interest_over_time()

        # Calculate date for 24 to 12 months ago (previous 12 months)
        previous_year_date = last_year_date - datetime.timedelta(days=365)
        previous_year_date_str = previous_year_date.strftime('%Y-%m-%d')

        # Build payload for the previous 12 months
        pytrends.build_payload([keyword], cat=0, timeframe=f'{previous_year_date_str} {last_year_date_str}', geo='RS', gprop='')
        data_previous_12_months = pytrends.interest_over_time()

        # Combine data using pd.concat
        combined_data = pd.concat([data_previous_12_months, data_last_12_months])


        if not combined_data.empty:
            # Calculate average interest
            average_interest = combined_data[keyword].mean()
            print(f"Average interest level for '{keyword}': {average_interest:.2f}")

            # Prepare data for linear regression
            combined_data['timestamp'] = np.arange(len(combined_data))  # Create a numerical index for the x-axis
            x = combined_data['timestamp']
            y = combined_data[keyword]

            # Calculate linear regression coefficients
            coefficients = np.polyfit(x, y, 1)  # 1 for linear
            linear_trend = np.polyval(coefficients, x)  # Evaluate the polynomial at the x points

            # Mark periods with interest above average and below a threshold (e.g., 90% of the max)
            smart_campaign_periods = combined_data[(combined_data[keyword] > average_interest) & 
                                                   (combined_data[keyword] < 0.9 * combined_data[keyword].max())]

            # Plotting the data
            plt.figure(figsize=(10, 5))
            plt.plot(combined_data.index, combined_data[keyword], label='Interest', marker='o')
            plt.plot(combined_data.index, linear_trend, color='red', linestyle='--', label='Trend Line')
            plt.axhline(y=average_interest, color='green', linestyle=':', label='Average Interest')

            # Highlighting the smartest time frame for a campaign
            plt.scatter(smart_campaign_periods.index, smart_campaign_periods[keyword], color='orange', 
                        label='Smart Campaign Periods', zorder=5)

            # Add average interest text on the chart
            plt.text(combined_data.index[-1], average_interest, f'Avg: {average_interest:.2f}', 
                    color='green', fontsize=10, ha='right')

            plt.title(f'Interest on Google Over Time for "{keyword}" in Serbia (Last 24 Months)')
            plt.xlabel('Date')
            plt.ylabel('Interest Level')
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid()
            plt.tight_layout()
                
            # Display the chart
            plt.show()

        else:
            print(f"No data available for the keyword: {keyword}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    keyword = input("Enter the keyword to search for trends: ")
    get_keyword_trends(keyword)
