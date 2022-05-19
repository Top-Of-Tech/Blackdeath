from colorama import init
from termcolor import colored
import sys
from src.threads import start_processes

init()

site = None
packets = None

if __name__ == "__main__":
    try:
        if "-h" in sys.argv or "--help" in sys.argv or "-help" in sys.argv:
            print(colored("\n[INFO] Usage: python3 blackdeath.py -s <site> -p <packets>", "green"))
            sys.exit(0)

        try:
            if "-s" in sys.argv and sys.argv.count("-s") == 1:
                site = sys.argv[sys.argv.index("-s") + 1]
        except:
            print(colored("[ERROR] Invalid site value", "red"))
        try:
            if "-p" in sys.argv and sys.argv.count("-p") == 1:
                packets = int(sys.argv[sys.argv.index("-p") + 1])
        except:
            print(colored("[ERROR] Invalid packets value", "red"))
        
        start_processes(site, packets)

    except KeyboardInterrupt:
        sys.exit()