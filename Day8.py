#!/usr/bin/env python

from collections import Counter

def main():
    # Day 8 
    with open('AoC_input.txt', 'r') as f:
        input_str = f.read()
    input_str = input_str.strip()

    px_width = 25
    px_height = 6
    px_layer = px_width * px_height

    layer = []
    layers = []
    layer_info = []

    px_count = 0
    for px in input_str:
        layer.append(int(px))
        px_count += 1
        if px_count == px_layer:
            px_count = 0
            layer_info.append(Counter(layer))
            layers.append(layer)
            layer = []

    layer_num = 0
    most_zero_layer = 0
    for layer in layer_info:
        if layer[0] < layer_info[most_zero_layer][0]: 
            most_zero_layer = layer_num
        layer_num += 1

    #print("Most zero layer: {}\nMultiplier = {}".format(most_zero_layer, layer_info[most_zero_layer][1] * layer_info[most_zero_layer][2]))

    image = []
    for pos in range(px_layer):
        image.append(get_pixel(pos, layers, 0))

    i = 0
    for px in image:
        print(px, end='')
        i += 1
        if i == px_width:
            print('')
            i = 0

def get_pixel(pos, layers, level):
    if layers[level][pos] == 2:
        return get_pixel(pos, layers, level+1)
    else:
        if layers[level][pos] == 1:
            return '#'
        else:
            return ' '


if __name__== "__main__":
    main()
