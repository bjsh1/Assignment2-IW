#8. Write a function, is_prime, that takes an integer and returns True
# If the number is prime and False if the number is not prime.

def is_prime(num):

    for numbers in range(2,num-1):
        
        if num%(numbers)==0:
            return False
        else:
            return True

print(is_prime(11))