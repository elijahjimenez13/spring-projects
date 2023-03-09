def multiSum(num1, num2): # this is a function that includes 2 parameter variables
    if num1 * num2 <= 1000: # this includes an if statement and that has a condition that states that num1 and num2 have to be lesst than or equal to so the if statement can be executed
        return num1 * num2 # if this function is true, it will return num1 * num2
    
    else: # if the statement is false
        return num1+num2 # this system will return num1 + num2
    
hope = multiSum(89, 54) # this is creating a variable that calls upon multiSum function that has 2 arguements that gives values to the 2 parameters (num1 and num2)
print(hope) # this prints whatever is returned from the function