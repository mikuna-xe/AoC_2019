#!/usr/bin/env python3

def main():
    # Day 2
    with open('AoC_input.txt', 'r') as f:
        input_str = f.read()
    input_list = input_str.strip().split(',')
    reset = list(map(int, input_list))
    opcode = reset.copy()

    # restore noun and verb
    noun = 1
    verb = 2

    opcode[noun] = 12
    opcode[verb] = 2

    for n in range(100):
        for v in range(100):
            opcode = reset.copy()
            # change input
            opcode[noun] = n
            opcode[verb] = v

            i = 0
            while 1:
                # addition
                if opcode[i] == 1:
                    opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
                    i = i+4

                # multiply
                elif opcode[i] == 2:
                    opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
                    i = i+4

                # halt
                elif opcode[i] == 99:
                    break

                else:
                    print("shit broke")
                    return

            if opcode[0] == 19690720:
                print("noun: {}, verb: {}".format(n, v))
                print("100 * n + v = {}".format(100*n+v))
                return


if __name__== "__main__":
    main()
