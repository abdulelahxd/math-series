def fibonacci(n):
    prev, next = (1,1)

    for i in range(0, n-2):
            prev, next = next, prev + next

    return(next)

def lucas(n):
    prev, next = (2,1)

    for i in range(0, n-2):
            prev, next = next, prev + next

    return(next)


def sum_series(n, num_one=0, num_two=1):

    if num_one == 0 and num_two == 1:
        return fibonacci(n)
    if num_one == 2 and num_two == 1:
        return lucas(n)
    
    
if __name__ == "__main__":
    n = int(input())