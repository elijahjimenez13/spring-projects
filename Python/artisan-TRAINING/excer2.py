print("Printing current and previous number sum in a range(10)")
def multiSum(current_num, prev_num, sum):
    while current_num < 9:
        current_num = current_num +1
        print(current_num)
        prev_num = current_num - 1
        sum = prev_num + current_num
        print(f'Current Number {current_num} Previous Number {prev_num} Sum: {sum}')
    

happy = multiSum(0,0,0)