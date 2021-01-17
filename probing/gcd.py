

def gcdCalculator(a,b):


    if a == 0 and b == 0:
        return 'please enter a number which is greater than 0'

    else:

        if b == 0:
            print('your gcd number is',a)

        else:

          mod_value = a % b
          gcdCalculator(b,mod_value)


if __name__ == "__main__":

     gcdCalculator(6,9)
