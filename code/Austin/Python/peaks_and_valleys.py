import itertools 
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaksandvalleys(terrain):
    p = []
    v = []
    p_v = []
    for i,x in list(enumerate(terrain))[1:-1]:
            firstneighbor = terrain[i-1]
            secondneighbor = terrain[i+1]
            if firstneighbor < x > secondneighbor:
                p.append(i)
                p_v.append(i)
            elif firstneighbor > x < secondneighbor:
                v.append(i)
                p_v.append(i)
    print(f"Peaks:{p}\nValleys:{v}\nPeaks And Valleys:{p_v}")

peaksandvalleys(data)
   
