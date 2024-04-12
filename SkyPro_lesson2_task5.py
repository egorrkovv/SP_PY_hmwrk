
def fizz_buzz(n):

    for n in range(1, n + 1):
        if (n % 3 == 0) and (n % 5 != 0):
            print("fizz")
        if (n % 5 == 0) and (n % 3 != 0):
            print("buzz")
        if (n % 3 == 0) and (n % 5 == 0):
            print("fizz_buzz")
        if (n % 3 !=0) and (n % 5 != 0):
            print(n)    
fizz_buzz(17)