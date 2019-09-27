import newModule
import time as t
start=t.time()
a=newModule.pyfib(30)
end=t.time()
print('cython:')
print('fib(30):',a)
print(f'{end-start}s')

