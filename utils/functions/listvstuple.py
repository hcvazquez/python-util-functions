import profile
import cProfile
import sys


def var_then_create_list(n):
    for _ in range(n):
        x,y,z=1,2,3
        [x,y,z]

def var_then_create_tuple(n):
    for _ in range(n):
        x,y,z=1,2,3
        [x,y,z]

def create_list(n):
    for _ in range(n):
        [1,2,3]

def create_tuple(n):
    for _ in range(n):
        (1,2,3)

def subs(coll):
    for i in range(len(coll)):
        for j in range(i+1, len(coll)+1):
            coll[i:j]

if __name__ == '__main__':
    print(sys.getsizeof({}))
    print(sys.getsizeof(set()))
    print(sys.getsizeof([]))
    print(sys.getsizeof(()))


    ten_millon_list = [x for x in range(10000)]
    ten_millon_tuple = tuple(ten_millon_list)
    print(sys.getsizeof(ten_millon_tuple))
    print(sys.getsizeof(ten_millon_list))
    cProfile.run('create_list(100000000),create_tuple(100000000)')
    cProfile.run('subs(ten_millon_list),subs(ten_millon_tuple)')
    cProfile.run('tuple(ten_millon_list)')
    cProfile.run('list(ten_millon_tuple)')