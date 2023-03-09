print("Printing current and previous number sum in a range(10)")
def multiSum(current_num, prev_num, sum):
    if current_num <= 10:
        current_num + 1
        prev_num = current_num - 1
        sum + current_num
        print(f'Current Number {current_num} Previous Number {prev_num} Sum: {sum}')

happy = multiSum(0,0,0)