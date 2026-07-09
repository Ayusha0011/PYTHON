try:
    numerator = int(input("Enter a number to divde"))
    denominator =int(input("Enter a number to divide by:"))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero IDIOT!")
except ValueError as e:
    print(e)
    print("ENTER ONLY NUMEROS POR FAVOR!!!!!!!!!!!!!!")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
     print(result)
finally:
    print("This will ALWAYS EXECUTE BIATCH")