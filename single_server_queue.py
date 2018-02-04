'Single server queue simulation'

from random import expovariate, gauss
from statistics import mean, median, stdev
#from termcolor import colored

def getServices(average_arrival_interval = 5.6, average_service_time = 5.0, stdev_service_time=0.5):
    
    num_waiting = 0
    arrivals = []
    starts = []
    arrival = service_end = 0

    for i in range(20000):
        if arrival <= service_end:
            num_waiting += 1
            arrival += expovariate(1.0 / average_arrival_interval)
            arrivals.append(arrival)
        else:
            num_waiting -= 1
            service_start = service_end if num_waiting else arrival
            service_time = gauss(average_service_time, stdev_service_time)
            service_end = service_start + service_time
            starts.append(service_start)
    waits = [start - arrival for arrival, start in zip(arrivals, starts)]
    print(f'Mean wait: {mean(waits) :.1f}. Stdev wait: {stdev(waits) :.1f}.')
    print(f'Median wait: {median(waits) :.1f}. Max wait: {max(waits) :.1f}.')
decoration = "##############################"
print(f"{decoration}Details with default parameters{decoration}")
getServices()
print(f"{decoration}Increasing the service efficieny by reducing average_service_time a little{decoration}")
getServices(average_service_time = 4.8)
print(f"{decoration}Becoming more consistent than efficient{decoration}")
getServices(stdev_service_time = 0.0)

