#!/usr/bin/env python3

def main():
    # Day 3
    with open('AoC_input.txt', 'r') as f:
        input_str = f.readlines()
    wire0 = input_str[0].strip().split(',')
    wire1 = input_str[1].strip().split(',')

    dir0 = []
    dir1 = []
    dist0 = []
    dist1 = []

    for cmd in wire0:
        dir0.append(cmd[0])
        dist0.append(int(cmd[1:]))

    for cmd in wire1:
        dir1.append(cmd[0])
        dist1.append(int(cmd[1:]))

    max_dim = 
    #print(dir0)
    #print(dir1)
    #print(dist0)
    #print(dist1)

if __name__== "__main__":
    main()
