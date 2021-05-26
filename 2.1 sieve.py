import timeit
import cProfile
import math

HOLE = 0



def prime(num):
    size = num ** 2 + 3
    if num > 5761455:
        raise Exception('Слишком большой аргумент')
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1_229: 10 ** 4,
               9_592: 10 ** 5,
               78_498: 10 ** 6,
               664_579: 10 ** 7,
               5_761_455: 10 ** 8,
               }
    for key in pi_func:
        if num <= key:
            size = pi_func[key]
            break

    array = [i for i in range(size)]

    array[1] = HOLE
    for i in range(2, size):
        if array[i] != HOLE:
            j = i + i

            while j < size:
                array[j] = HOLE
                j += i

    res = [i for i in array if i != HOLE]
    return res[num - 1]


print(prime(1))

number = 1
while number < 4000:
    number *= 2
    t_it = timeit.timeit('prime(number)', number=1000, globals=globals())
    print(f"{number=}\t{t_it=}\t{t_it / number =}")

# number=2	t_it=0.007081705000000001	t_it / number =0.0035408525000000003
# number=4	t_it=0.004341559000000002	t_it / number =0.0010853897500000004
# number=8	t_it=0.031702312	t_it / number =0.003962789
# number=16	t_it=0.037186553	t_it / number =0.0023241595625
# number=32	t_it=0.366951441	t_it / number =0.01146723253125
# number=64	t_it=0.32198935700000003	t_it / number =0.0050310837031250005
# number=128	t_it=0.31411978799999996	t_it / number =0.0024540608437499997
# number=256	t_it=3.6919942719999996	t_it / number =0.014421852624999999
# number=512	t_it=3.5112782549999997	t_it / number =0.006857965341796874
# number=1024	t_it=3.6823138760000003	t_it / number =0.0035960096445312503
# number=2048	t_it=46.098864115	t_it / number =0.022509210993652343
# number=4096	t_it=45.756522611	t_it / number =0.011171026028076172


cProfile.run('prime(10000)')
# 6 function calls in 0.516 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.009    0.009    0.516    0.516 <string>:1(<module>)
#         1    0.068    0.068    0.068    0.068 scratch_59.py:27(<listcomp>)
#         1    0.035    0.035    0.035    0.035 scratch_59.py:38(<listcomp>)
#         1    0.404    0.404    0.506    0.506 scratch_59.py:9(prime)
#         1    0.000    0.000    0.516    0.516 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



print(timeit.timeit('prime(1228)', number=1000, globals=globals()))
# 3.515681846999996

print(timeit.timeit('prime(1230)', number=1000, globals=globals()))
# 44.666476351