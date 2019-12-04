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
    dict0 = dict()
    start = (0,0)
    step_count = 0
    for dir, dist in zip(dir0, dist0):
        start, line, step_count, steps = add_coords(start, dir, dist, step_count, dict0)
        set0.update(line)
        dict0 = steps

    set1 = set()
    dict1 = dict()
    start = (0,0)
    step_count = 0
    for dir, dist in zip(dir1, dist1):
        start, line, step_count, steps = add_coords(start, dir, dist, step_count, dict1)
        set1.update(line)
        dict1 = steps

    cross = set0.intersection(set1)
    cross2 = set0.intersection(set1)

    ### Get closest manhattan distance ###
    closest = (9999,9999)
    for x in range(len(cross)):
        point = cross.pop()
        if get_dist(point) < get_dist(closest):
            closest = point

    print("Closest intersection point: {}\nDistance: {}".format(closest, get_dist(closest)))

    ## Get least steps ###
    closest = (9999,9999)
    least_steps = 9999999
    for x in range(len(cross2)):
        point = cross2.pop()
        steps = steps_to_point(dict0, dict1, point)
        if steps < least_steps:
            least_steps = steps
            closest = point

    print("Least steps intersection point: {}\nDistance: {}".format(closest, least_steps))


def steps_to_point(dict0, dict1, point):
    return dict0['({},{})'.format(point[0],point[1])] + dict1['({},{})'.format(point[0],point[1])]

def get_dist(point):
    return abs(point[0]) + abs(point[1])


def add_coords(start, dir, dist, step_count, line_steps):
    line = set()
    ox = start[0]
    oy = start[1]

    if dir == 'U':
        for y in range(oy+1, oy+1+dist):
            step_count += 1
            line.add((ox,y))
            if '{},{}'.format(ox,y) in line_steps:
                line_steps['({},{})'.format(ox,y)].append(step_count)
            else:
                line_steps['({},{})'.format(ox,y)] = step_count
        return (ox,y), line, step_count, line_steps

    elif dir == 'D':
        for y in range(oy-1, oy-1-dist, -1):
            step_count += 1
            line.add((ox,y))
            if '{},{}'.format(ox,y) in line_steps:
                line_steps['({},{})'.format(ox,y)].append(step_count)
            else:
                line_steps['({},{})'.format(ox,y)] = step_count
        return (ox,y), line, step_count, line_steps

    elif dir == 'L':
        for x in range(ox-1, ox-1-dist, -1):
            step_count += 1
            line.add((x,oy))
            if '{},{}'.format(x,oy) in line_steps:
                line_steps['({},{})'.format(x,oy)].append(step_count)
            else:
                line_steps['({},{})'.format(x,oy)] = step_count
        return (x,oy), line, step_count, line_steps

    elif dir == 'R':
        for x in range(ox+1, ox+1+dist):
            step_count += 1
            line.add((x,oy))
            if '{},{}'.format(x,oy) in line_steps:
                line_steps['({},{})'.format(x,oy)].append(step_count)
            else:
                line_steps['({},{})'.format(x,oy)] = step_count
        return (x,oy), line, step_count, line_steps

    else:
        raise AssertionError("sth fucked up. Bad dir: {}".format(dir))


if __name__== "__main__":
    main()
