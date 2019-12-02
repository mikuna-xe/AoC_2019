#!/usr/bin/env python

def get_total_fuel(input):
    fuel = input/3 - 2

    if fuel <= 0:
        return 0
    else:
        return fuel + get_total_fuel(fuel)

def main():
    # Day 2 - Part 1
    with open('AoC_input.txt', 'r') as f:
        input_str = f.read()
    input_list = input_str.strip().split(',')
    opcode = list(map(int, input_list))
    
    # restore gravity assist
    opcode[1] = 12
    opcode[2] = 2
    
    ind = 0
    
    cmd_ind = range(len(opcode))[0::4]
    print(cmd_ind)

    for i in cmd_ind:
        print("index: {}".format(i))

        # addition
        if opcode[i] == 1:
            print("add: [{}] + [{}] = [{}]".format(opcode[i+1], opcode[i+2], opcode[i+3]))
            opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
            print(">> {} + {}".format(opcode[opcode[i+1]], opcode[opcode[i+2]]))

        # multiply
        elif opcode[i] == 2:
            print("multiply: [{}] x [{}] = [{}]".format(opcode[i+1], opcode[i+2], opcode[i+3]))
            opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
            print(">> {} x {}".format(opcode[opcode[i+1]], opcode[opcode[i+2]]))

        # halt
        elif opcode[i] == 99:    
            print("halt")
            break

    print("opcode: \n{}".format(opcode))

if __name__== "__main__":
    main()
