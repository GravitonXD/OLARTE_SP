import requests
from os import makedirs
def connection_test():
    server_ip = input("Enter the server IPv4 address: ")
    base_url = f'http://{server_ip}:8000'

    home_req = requests.get(f'{base_url}/home/')
    if home_req.status_code == 200:
        print('Connected to the server.')
        return server_ip
    else:
        print('Unable to connect to the server. Please enter a valid IPv4 address.')
        connection_test()

def load_test(url, num_of_requests, endpoint, name):
    for i in range(num_of_requests):
        r = requests.get(url)
        with open(f'./results/{name}/res_{endpoint}_{num_of_requests}.csv', 'a') as f:
            f.write(f'{i+1}, {1 if r.status_code == 200 else 0}\n')
        print(f'{i+1} of {num_of_requests} completed.')

def welcome():
    print("""
    Welcome to the load testing program.\n
    This program will run a load based test on the alamAPI developed by John Markton Olarte.\n
    For more info about this tester and alamSYS, you may contact the developer at:\n
    jmolarte@up.edu.ph\n\n

    NOTE: Please make sure to read the INSTRUCTIONS.txt file before running this program.\n\n
    NOTE: THIS PROGRAM WILL NOT COLLECT ANY DATA FROM THE USER.\n\n

    To continue, press ENTER. To exit, press CTRL+C.\n
    """)
    input()
    

def main():
    welcome()
    name = input("Enter your name: ")
    makedirs(f'./results/{name}', exist_ok=True)
    server_ip = connection_test()
    base_url = f'http://{server_ip}:8000'

    list_of_requests = [100, 1000]
    
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

if __name__ == '__main__':
    main()