def fib(n=int):
    if n<2:return n

    a=0
    b=1
    for i in range(n-1):
        a,b=b,a+b
    return b

import time as t
start=t.time()
c=fib(30)
end=t.time()
print(f'''python:
fib(30): {c}
{end-start}s''')