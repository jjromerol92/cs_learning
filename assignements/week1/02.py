from multiprocessing.resource_tracker import ResourceTracker


def add_all_even_div_three(n):
    """
    Return the sum of all even numbers from 1 to n that are divisible by 3.

    >>> add_all_even_div_three(10) # 6
    6
    >>> add_all_even_div_three(20) # 6 + 12 + 18
    36
    >>> add_all_even_div_three(30) # 6 + 12 + 18 + 24 + 30
    90
    """
    suma = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 2 == 0:
                suma += i

    return suma

def fizzbuzz(n):
    """
    Print the numbers from 1 to n, replacing:
    - multiples of 3 with "fizz"
    - multiples of 5 with "buzz", and
    - multiples of both with "fizzbuzz".

    >>> fizzbuzz(1)
    1
    >>> fizzbuzz(3)
    1
    2
    fizz
    >>> fizzbuzz(5)
    1
    2
    fizz
    4
    buzz
    >>> fizzbuzz(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    """
    for i in range(1, n + 1):
        if i%3 == 0 and i%5 == 0:
            print("fizzbuzz")
            continue
        if i%3  == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)


# NOTE: This is Lab 01 optional question (Q10)
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    return sum(int(digit) for digit in str(y))
