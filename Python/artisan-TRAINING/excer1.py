def multiSum(num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    
    else:
        return num1+num2
    
hope = multiSum(89, 54)
print(hope)