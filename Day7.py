#!/usr/bin/env python

import itertools

def main():
    # Day 7 
    with open('AoC_input.txt', 'r') as f:
        input_str = f.read()

    input_list = input_str.strip().split(',')
    OG = list(map(int, input_list))
    programs = [OG.copy(), OG.copy(), OG.copy(), OG.copy(), OG.copy()]

    #phase_settings = list(itertools.permutations([0,1,2,3,4]))
    phase_settings = list(itertools.permutations([5,6,7,8,9]))
    output_signals = []

    amp_input = 0
    positions = [0,0,0,0,0]
    for permutation in phase_settings:
        amp_input = 0
        programs = [OG.copy(), OG.copy(), OG.copy(), OG.copy(), OG.copy()]
        phase_input_flag = 1
        halted = False
        while not halted:
            amp = 0
            for phase, program, pos in zip(permutation, programs, positions):
                amp_input, new_pos, halted = amplifier(program, phase, amp_input, phase_input_flag, pos)
                positions[amp] = new_pos
                if amp_input:
                    amp_output = amp_input
                amp += 1

            if halted:
                output_signals.append(amp_output)

            phase_input_flag = 0
            

    print("Max signal: {}".format(max(output_signals)))


def amplifier(program, phase, TEST_input, phase_input_flag=0, i=0):
    output_flag = 0
    #i = 0
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
            i = i+4

        # multiply
        elif opcode == 2:
            program[program[i+3]] = a * b
            i = i+4

        # input
        elif opcode == 3:
            if phase_input_flag:
                program[program[i+1]] = phase
                phase_input_flag = 0
            else:
                program[program[i+1]] = TEST_input
            i = i+2

        # output
        elif opcode == 4:
            #print("TEST_output: {}".format(a))
            i = i+2
            return a, i, False

        # Jump if true
        elif opcode == 5:
            if a:
                i = b
            else:
                i = i+3

        # Jump if false
        elif opcode == 6:
            if not a:
                i = b
            else:
                i = i+3

        # Less than
        elif opcode == 7:
            if a < b:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            i = i+4

        # Equals
        elif opcode == 8:
            if a == b:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            i = i+4

        # halt
        elif opcode == 9:
            return None, 0, True

        else:
            print("shit broke")
            return


if __name__== "__main__":
    main()
