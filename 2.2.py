import timeit
import cProfile


def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, current_prime):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime


print(prime(2))

number = 1
while number < 256:
    number *= 2
    t_it = timeit.timeit('prime(number)', number=1000, globals=globals())
    print(f"{number=}\t{t_it=}\t{t_it / number =}")

# number=2	t_it=0.0009352450000000012	t_it / number =0.0004676225000000006
# number=4	t_it=0.0042234190000000026	t_it / number =0.0010558547500000006
# number=8	t_it=0.014076481999999994	t_it / number =0.0017595602499999993
# number=16	t_it=0.048390920999999996	t_it / number =0.0030244325624999998
# number=32	t_it=0.16265950899999998	t_it / number =0.005083109656249999
# number=64	t_it=0.7163758339999999	t_it / number =0.011193372406249999
# number=128	t_it=3.257185225	t_it / number =0.0254467595703125
# number=256	t_it=14.343681744000001	t_it / number =0.056030006812500005


cProfile.run('prime(10000)')
#       4 function calls in 36.249 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   36.249   36.249 <string>:1(<module>)
#         1   36.249   36.249   36.249   36.249 without_sieve.py:5(prime)
#         1    0.000    0.000   36.249   36.249 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
