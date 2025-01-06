import argparse
from threading import Thread
import time
from collections import defaultdict
from utils import parse_config, check_health, log_availability

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str, help="Path to the config file (YAML format)")
    args = parser.parse_args()

    endpoints = parse_config(args.config_file)
    domain_stats = defaultdict(lambda: {'up': 0, 'total': 0})

    try:
        while True:
            threads = []
            for endpoint in endpoints:
                thread = Thread(target=check_health, args=(endpoint, domain_stats))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            log_availability(domain_stats)

            time.sleep(15)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
