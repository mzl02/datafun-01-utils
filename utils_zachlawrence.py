
#####################################
# Import Libraries 
#####################################
import statistics
from datetime import date


#####################################
# Company Data Defined 
#####################################

has_international_clients: bool = True
years_in_operation: int = 10
average_client_satisfaction: float = 4.7
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#####################################
# Statistical Calculations for Company Data 
#####################################
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

#####################################
# Additional Varibles
#####################################
offers_clients_additional_skillsets = True
skillsets: list = ["Cyber","Database Design, Implimitation, Optimization and Support","Network Support","Vuln Assessments"]
current_headcount: float = 4.5
#####################################
# Date Range
#####################################
closing_price_date_range_start: date = date(2023, 8, 29)
closing_price_date_range_end: date = date(2024, 8, 29)

#####################################
# Daily Closing Price Corn Futures
#####################################
corn_prices_daily_closing = [
    371.75, 365.25, 367.25, 362.00, 367.75, 371.50, 375.50, 375.00, 378.00, 370.50, 
    375.00, 381.00, 377.75, 383.25, 376.75, 379.25, 383.25, 388.75, 390.75, 386.50, 
    382.00, 382.75, 388.75, 396.25, 394.50, 406.00, 403.75, 402.50, 400.25, 390.50, 
    391.25, 398.00, 395.75, 390.50, 400.00, 406.75, 403.25, 400.25, 395.75, 411.25, 
    403.50, 402.00, 398.25, 397.25, 413.75, 420.00, 425.50, 433.50, 435.00, 439.75, 
    450.00, 443.75, 450.00, 458.50, 454.25, 449.50, 451.75, 448.75, 452.00, 439.25, 
    442.50, 443.50, 446.25, 448.75, 455.25, 462.50, 464.75, 464.00, 461.25, 458.00, 
    460.50, 452.50, 457.00, 462.50, 453.75, 458.50, 455.75, 442.75, 445.50, 453.75, 
    457.00, 447.00, 452.00, 443.25, 439.50, 439.25, 440.00, 441.00, 437.75, 443.00, 
    439.75, 433.50, 426.75, 430.25, 431.00, 431.50, 435.50, 428.75, 434.25, 431.25, 
    435.50, 434.25, 435.25, 431.75, 426.50, 435.50, 442.00, 426.75, 432.50, 437.75, 
    439.25, 440.75, 439.00, 439.50, 436.00, 436.75, 422.50, 426.50, 429.00, 428.25, 
    426.25, 426.00, 418.00, 413.50, 417.50, 412.25, 415.75, 413.25, 408.25, 407.00, 
    399.75, 406.00, 411.00, 418.75, 416.50, 417.75, 424.25, 430.75, 430.50, 429.00, 
    433.25, 434.25, 438.75, 443.00, 442.75, 447.25, 448.25, 447.75, 440.25, 446.25, 
    451.75, 452.25, 446.50, 445.75, 445.50, 444.00, 442.25, 443.50, 447.00, 457.75, 
    459.50, 459.25, 455.00, 460.75, 466.50, 465.25, 463.75, 471.25, 474.25, 476.50, 
    480.25, 473.00, 472.50, 469.75, 472.75, 477.00, 483.00, 456.75, 456.75, 462.50, 
    460.50, 465.75, 468.25, 464.75, 468.50, 460.25, 464.50, 461.75, 449.75, 451.50, 
    455.50, 463.25, 468.75, 470.00, 469.50, 467.00, 474.75, 470.75, 478.25, 477.25, 
    464.00, 468.00, 476.00, 468.50, 477.75, 477.25, 470.00, 475.00, 478.75, 478.25, 
    480.75, 479.25, 480.00, 484.00, 490.25, 495.50, 505.00, 492.00, 489.00, 490.00, 
    493.25, 496.00, 488.00, 485.50, 488.25, 492.00, 497.50, 486.00, 487.50, 488.75, 
    476.75, 488.50, 483.25, 479.75, 481.25, 477.25, 475.25, 482.25, 476.25, 471.50, 
    476.25, 462.50, 464.00, 463.25, 471.25, 468.50, 470.75, 471.50, 471.00, 464.75, 
    461.00, 461.75, 469.50
]

#####################################
# Statistical Data for Corn based on Closing Price
#####################################

min_price: float = min(corn_prices_daily_closing)  
max_price: float = max(corn_prices_daily_closing)  
mean_price: float = statistics.mean(corn_prices_daily_closing)  
stdev_price: float = statistics.stdev(corn_prices_daily_closing)
#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Millennium Group: Delivering Professional Insights For The Financial Markets'

#####################################
# F-String Defined
#####################################
byline: str = f"""
----------------------------------------------------------------------------
Millennium Group: Delivering Professional Insights For The Financial Markets
----------------------------------------------------------------------------
Has International Clients:     {has_international_clients}
Years in Operation:            {years_in_operation}
Skills Offered:                {skills_offered}
Client Satisfaction Scores:    {client_satisfaction_scores}
Minimum Satisfaction Score:    {min_score}
Maximum Satisfaction Score:    {max_score}
Mean Satisfaction Score:       {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}

Corn Market Statistical Examples:
Corn Daily Close Statistics From:  {closing_price_date_range_start} to {closing_price_date_range_end}
Minimum Daily Close:               {min_price}
Maximum Daily Close:               {max_price}
Mean Closing Price:                {round(mean_price, 2)}
Standard Deviation:                {round(stdev_price, 2)}


"""


#####################################
# Define a main() function for this module.
#####################################
def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())
#####################################
# Define get_byline() function for this module.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
