import csv
from itertools import permutations as per
mylist = []
def goodprint(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
    return 0
with open('2_2_christmas_shopping.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mylist.append(row)
        
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        if('-' in mylist[i][j]):
            mylist[i][j] = 1000
        else:
            mylist[i][j]=int(mylist[i][j])

goodprint(mylist)

track = []

group = [[1,2],[3,4],[5,6],[7,8],[9,10]]
pre_group = []
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    pre_group.append([group[0][a], group[1][b], group[2][c], group[3][d], group[4][e]])
pre_per = []
for pGroup in pre_group:
    pre_per+= list(per(pGroup))
for oneTrack in pre_per:
        track.append(list(oneTrack))

for i in range(len(track)):
    track[i].append(11)
    track[i].insert(0,0)

min_track =10000
cost_track = 0
index_track = []

for oneTrack in track:
    for i in range(6):
        cost_track+=mylist[oneTrack[i]][oneTrack[i+1]]
    if(cost_track<= min_track):
        min_track = cost_track
        index_track = oneTrack
    cost_track=0
        
print("the lowest cost track is: " + str(min_track)+ "\nroute = " +str(index_track))
