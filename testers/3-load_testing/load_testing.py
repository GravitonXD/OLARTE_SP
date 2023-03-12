import requests
import datetime
from os import makedirs
import schedule
from time import sleep

def load_test(url, num_of_requests, endpoint, name):
    # Write the starting time
    start_time = datetime.datetime.now()
    with open(f'./results/{name}/res_{endpoint}_{num_of_requests}.csv', 'w') as f:
        f.write(f'Start time: {start_time}\n')
        f.write(f'Number of requests: {num_of_requests}\n')
        f.write(f'Endpoint: {endpoint}\n')
        f.write(f'Name: {name}\n')
        f.write('Request number, Status code\n')

    # Run the load test
    for i in range(num_of_requests):
        r = requests.get(url)
        with open(f'./results/{name}/res_{endpoint}_{num_of_requests}.csv', 'a') as f:
            f.write(f'{i+1}, {1 if r.status_code == 200 else 0}\n')
        print(f'{i+1} of {num_of_requests} completed.')
    
    # Write the ending time
    end_time = datetime.datetime.now()
    with open(f'./results/{name}/res_{endpoint}_{num_of_requests}.csv', 'a') as f:
        f.write(f'End Time: {end_time}\n')
        f.write(f'Total Run Time: {end_time - start_time}\n')

def welcome():
    print("""
    Welcome to the load testing program.\n
    This program will run a load based test on the alamAPI developed by John Markton Olarte.\n
    For more info about this tester and alamSYS, you may contact the developer at:\n
    jmolarte@up.edu.ph\n\n

    NOTE: Please make sure to read the INSTRUCTIONS.txt file before running this program.\n\n
    NOTE: THIS PROGRAM WILL NOT COLLECT ANY DATA FROM THE USER.\n\n

    THIS PROGRAM WILL RUN AT EXACTLY 10:30 AM AND IS ESTIMATED TO RUN FOR 2 HOURS.\n
    """)

def random_string(length):
    import random
    import string
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def scheduled_task():
    # Generate a random string for the name of the folder
    name = random_string(10)
    makedirs(f'./results/{name}', exist_ok=True)

    base_url = f'https://alam.ap.loclx.io'

    list_of_requests = [10, 100, 1_000]
    
    print("Running load test, please wait...\n")
    # Testing for stocks to buy endpoint
    buy_url = f'{base_url}/stocks_to_buy/all/'
    for num_of_requests in list_of_requests:
        print(f'Running {num_of_requests} requests to {buy_url}')
        load_test(buy_url, num_of_requests, 'buy', name)

    # Testing for stocks to sell endpoint
    sell_url = f'{base_url}/stocks_to_sell/all/'
    for num_of_requests in list_of_requests:
        print(f'Running {num_of_requests} requests to {sell_url}')
        load_test(sell_url, num_of_requests, 'sell', name)

    print("Load test completed.\n")
    
def main():
    welcome()

    print("Waiting for schedule...\n")
    schedule.every().day.at("10:30").do(scheduled_task)

    while True:
        schedule.run_pending()
        # Print remaining time before scheduled task
        print(f'Next scheduled task in {schedule.idle_seconds()} seconds.', end='\r')
        sleep(1)

if __name__ == '__main__':
    main()