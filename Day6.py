#!/usr/bin/env python

def main():
    # Day 5 
    with open('AoC_input.txt', 'r') as f:
        input_str = f.readlines()
    
    relationships = list(map(str.strip, input_str))

    # planets['child'] = 'parent'
    planets = {}
    
    for orbital in relationships:
        parent = orbital.split(')')[0]
        child = orbital.split(')')[1]
        planets[child] = parent

    total = 0
    for child, parent in planets.items():
        if child == "SAN":
            SAN = get_orbital_chain(parent, planets)
        elif child == "YOU":
            YOU = get_orbital_chain(parent, planets)
        #total += len(chain)
    #print("Total orbits: {}".format(total))
    
    path = set(SAN)^set(YOU)
    #print(path)
    print("Path length: {}".format(len(path)))


def get_orbital_chain(orbit_parent, planets):
    if orbit_parent not in planets.keys():
        # has no parent planet, is orbit centre
        return orbit_parent
    else:
        # has parent planet
        link = get_orbital_chain(planets[orbit_parent], planets)
        chain = [orbit_parent]
        if isinstance(link, str):
            chain.append(link)
        else:
            chain.extend(link)
        return chain


def get_orbit_count(orbit_parent, planets):
    if orbit_parent not in planets.keys():
        # has no parent planet, is orbit centre
        return 1
    else:
        # has parent planet
        arr = [orbit_parent]
        return 1 + get_orbit_count(planets[orbit_parent], planets)




if __name__== "__main__":
    main()
