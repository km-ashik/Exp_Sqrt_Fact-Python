#Exponentiation
def exp():
    print("\n-----------------FIND THE EXPONENTIATION------------------")
    number = int(input("EXPONENT NUMBER ="))
    power = float(input("POWER ="))
    result = number ** power
    print("EXPONTATION = ",result)

    # if number=2, power=3
    # exponentiation means 2*2*2 = 8
exp()    

def factorial():
    print("\n---------------FIND THE FACTORIAL-------------")
    n = int(input("ENTER THE NUMBER = "))
    def fact(n):
        # print(n)
        if n == 1:
            return 1
        else :
            return n * fact(n-1)
    print(f"FACTORIAL OF {n} IS =",fact(n))

    # if the number is 5 
    # the factoral is 5*4*3*2*1 = 120
factorial()    

def sq_root():
    print("\n---------------FIND THE SQUARE ROOT-----------------")
    n = int(input("ENTER THE NUMBER = "))
    r= round( n ** 0.5,2)
    print(f"ROOT OF {n} IS = {r}")

    # square root of the n is n raised to the  power 0.5 
    # square root of 20 = 20 raised to the power 0.5 = 

sq_root()

