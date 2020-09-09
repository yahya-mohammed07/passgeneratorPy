import random as rand

def main():
    data ="a@blT5m4*nNy3z_0&2oD0p5Gw+E1#c2Zh1-BCvS6wB$~Hxi7jNk%dTUe5fr8X#%de5frGUIXs0Dt/9uL%gE!1GZH#c2h1Cv6wB$FCv6wB$HxiHm4*ny&3Dz_0S@O"
    size = int(input("-enter the size of the password: "))
    generator(data,size)

def generator(data, size):
    result = ""
    for i in range(size):
        result += data[rand.randint(0,len(data))]
    print(result)
    return i

main()