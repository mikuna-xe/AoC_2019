#!/usr/bin/env python

# Day 1 - Part 2
def get_total_fuel(input):
    fuel = input/3 - 2

    if fuel <= 0:
        return 0
    else:
        return fuel + get_total_fuel(fuel)

def main():
    # Day 1 - Part 1
    with open('AoC_input.txt', 'r') as f:
        input_list = f.readlines()
    input_list = map(int, input_list)

    fuel_total = 0
    for mass in input_list:
        #fuel = mass/3 - 2
        fuel = get_total_fuel(mass)
        fuel_total = fuel_total + fuel
    print("final: {}".format(fuel_total))

if __name__== "__main__":
    main()
