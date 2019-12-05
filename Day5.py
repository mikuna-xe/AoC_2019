#!/usr/bin/env python

def main():
    # Day 5 
    with open('AoC_input.txt', 'r') as f:
        input_str = f.read()

    input_list = input_str.strip().split(',')
    program = list(map(int, input_list))

    TEST_input = 5
    output_flag = 0

    i = 0
    while 1:
        # Get opcode and modes
        opcode = program[i] % 10
        mode1 = program[i] // 100 % 10   
        mode2 = program[i] // 1000 % 10   
        mode3 = program[i] // 10000 % 10   

        if opcode not in (3,9):
            if mode1:
                a = program[i+1]
            else:
                a = program[program[i+1]]

        if opcode not in (3,4,9):
            if mode2:
                b = program[i+2]
            else:
                b = program[program[i+2]]

        # addition
        if opcode == 1:
            program[program[i+3]] = a + b
            output_flag = 0
            i = i+4

        # multiply
        elif opcode == 2:
            program[program[i+3]] = a * b
            output_flag = 0
            i = i+4

        # input
        elif opcode == 3:
            program[program[i+1]] = TEST_input
            output_flag = 0
            i = i+2

        # output
        elif opcode == 4:
            print("TEST_output: {}".format(a))
            output_flag = 1
            i = i+2

        # Jump if true
        elif opcode == 5:
            if a:
                i = b
            else:
                i = i+3
            output_flag = 1

        # Jump if false
        elif opcode == 6:
            if not a:
                i = b
            else:
                i = i+3
            output_flag = 1

        # Less than
        elif opcode == 7:
            if a < b:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            output_flag = 1
            i = i+4

        # Equals
        elif opcode == 8:
            if a == b:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            output_flag = 1
            i = i+4

        # halt
        elif opcode == 9:
            if output_flag:
                print("Output flag set when halted. Done.")
            else:
                print("Output flag not set when halted. Error in program.")
            break

        else:
            print("shit broke")
            return


if __name__== "__main__":
    main()
