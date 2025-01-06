import yaml
import requests
import time
from collections import defaultdict

#Function to parse yaml file
def parse_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

#Function to check health of single endpoint
def check_health(endpoint, domain_stats):
    url = endpoint['url']
    method = endpoint.get('method', 'GET').upper()
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)

    try:
        start_time = time.time()
        if method == 'GET':
            response = requests.get(url, headers=headers, timeout=5)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=body, timeout=5)
        else:
            print(f"method not supported: {method} for {url}")
            return

        latency = (time.time() - start_time) * 1000
        status = "UP" if 200 <= response.status_code < 300 and latency < 500 else "DOWN"

    except requests.exceptions.RequestException:
        status = "DOWN"

    domain = url.split('/')[2]
    domain_stats[domain]['total'] += 1
    if status == "UP":
        domain_stats[domain]['up'] += 1

#Function to log availability
def log_availability(domain_stats):
    for domain, stats in domain_stats.items():
        availability = 100 * stats['up'] / stats['total']
        print(f"{domain} has {availability:.0f}% availability percentage")