#!/usr/bin/env python3

def main():
    # Day 4
    with open('AoC_input.txt', 'r') as f:
        input_str = f.read()

    lower = list(map(int, input_str.split('-')))[0]
    upper = list(map(int, input_str.split('-')))[1]

    count = 0
    for num in range(lower,upper):
        digits = list(map(int,str(num)))

        if is_double_only(digits) and is_increase(digits):
            count += 1

    print("Count: {}".format(count))

def is_double(num_arr):
    for i in range(len(num_arr)-1):
        if num_arr[i] == num_arr[i+1]:
            return True
    return False

def is_double_only(num_arr):
    ctr = 10 * [0]
    for i in num_arr:
        ctr[i] += 1

    if 2 in ctr:
        return True
    else:
        return False

def is_increase(num_arr):
    for i in range(len(num_arr)-1):
        if num_arr[i] > num_arr[i+1]:
            return False
    return True


if __name__== "__main__":
    main()
