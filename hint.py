from typing import *
from collections import OrderedDict, deque
x = 10                    # type: int
'''y = 10                    # type: str'''


def f(x: int,y: int) -> int:
    return x+y

print(f(10,12))
#print(f(10, 'amit'))

#x = OrderedDict()                    # type: OrderedDict


def g(x: Sequence[int]) -> None:
    print(len(x))
    print(x[2])

    for i in x:
        print(i)
    print()
def h(x: List[int]) -> None:
    print(len(x))
    print(x[2])

    for i in x:
        print(i)
    print()


g([1,2,3,4])
# g('ansdcd')
g((12,34,43))
h([1,2,3,4])
# g('ansdcd')
#h((12,34,43))


hts = [97.1, 102.5, 97.5]     #type: List[float]

person = ('Rasas',2323)       #type: Tuple[str, float]

info = ('asas','asdsd','fdsfasa','sdasds')   # type: Tuple[str, ...]


fifo = deque()                  # type: deque

print(f'The answer is {x} today')


Point = NamedTuple('Point',[('x', int),('y',int)])
