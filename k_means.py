from math import fsum, sqrt
from typing import Iterable, Tuple
from dis import dis
from collections import defaultdict
from functools import partial
from pprint import pprint

Point = Tuple[int, ...]
points = [(10,20,30),
          (20,30,40),
          (30,40,50),
          (40,50,60),
          (25,35,45),
          (5,15,25)]
centroid = [(10,20,30),
          (20,30,40)]
def mean(data: Iterable[float]) -> float:
    data = list(data)
    return fsum(data)/len(data)

print(mean([10,20,30]))


def dist(p: Point,q: Point, sum = fsum, sqrt = sqrt, zip = zip) -> float:
    'Euclidean distance between multi dimensional data'
    return sqrt(sum((x-y)**2 for x,y in zip(p,q)))

#dis(dist)

for point in points:
    print(point, dist(point, (0, 0, 0))) 


def assign_data(centroid, data) -> defaultdict:
    d = defaultdict(list)
    for point in data:
        #closest_centroid = min(centroid, key = lambda centroid: dist(point, centroid))
        closest_centroid = min(centroid, key = partial(dist, point))
        d[closest_centroid] .append(point)
    return d

def compute_groups(groups):
    '''Compute the centroid of each group'''
    return [tuple(map(mean, zip(*groups))) for group in groups]

