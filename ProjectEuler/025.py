#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def get_fib(n):
    fibPrev = 0
    fibCurrent = 1
    fibResult = fibPrev + fibCurrent
    cnt = 1


    while len(str(fibResult)) < n:
        print(fibResult)
        fibResult = fibPrev + fibCurrent
        fibPrev = fibCurrent
        fibCurrent = fibResult
        cnt +=1





    return fibResult, cnt
print(get_fib(1000))
