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

    set0 = set()
    start = (0,0)
    for dir, dist in zip(dir0, dist0):#zip(['U', 'R'], [5,3]):
        start, line = add_coords(start, dir, dist)
        set0.update(line)


    set1 = set()
    start = (0,0)
    for dir, dist in zip(dir1, dist1):
        start, line = add_coords(start, dir, dist)
        set1.update(line)

    cross = set0.intersection(set1)

    closest = (9999,9999)
    for x in range(len(cross)):
        point = cross.pop()
        if get_dist(point) < get_dist(closest):
            closest = point

    print("Closest intersection point: {}\nDistance: {}".format(closest, get_dist(closest)))


def get_dist(point):
    return abs(point[0]) + abs(point[1])


def add_coords(start, dir, dist):
    line = set()
    ox = start[0]
    oy = start[1]

    if dir == 'U':
        for y in range(oy+1, oy+1+dist):
            line.add((ox,y))
        return (ox,y), line

    elif dir == 'D':
        for y in range(oy-1, oy-1-dist, -1):
            line.add((ox,y))
        return (ox,y), line

    elif dir == 'L':
        for x in range(ox-1, ox-1-dist, -1):
            line.add((x,oy))
        return (x,oy), line

    elif dir == 'R':
        for x in range(ox+1, ox+1+dist):
            line.add((x,oy))
        return (x,oy), line

    else:
        raise AssertionError("sth fucked up. Bad dir: {}".format(dir))

if __name__== "__main__":
    main()
