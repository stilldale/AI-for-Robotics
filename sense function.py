p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2
q = [0, 0, 0, 0, 0]

def sense(p, Z):
    for i in range(len(world)):
        if world[i] == Z:
            q[i] = pHit * p[i]
        else:
            q[i] = pMiss * p[i]

    return q
    
print sense(p,Z)
