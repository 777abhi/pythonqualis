#Define the generator function factorial_gen, which is capable of yielding factorial values of natural numbers.
#Create a generator fs from factorial_gen.
#Ensure, the first two values to be yielded by fs are 1 and 1, corresponding to factorial of 0 and 1 respectively.
#Call next method on fs and print the returned value.
#Repeat the above step 3 more times, and display each returned value in a separate line.

def factorial_gen(x):
    a = 1
    print(1)
    for i in range(1, x+1):
        a *= i
        yield a

fs = factorial_gen(10)

print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))