import csv
from itertools import permutations as per
mylist = []
def goodprint(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
    return 0
with open('1_2_christmas_cards.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mylist.append(row)
        
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        if('-' in mylist[i][j]):
            mylist[i][j] = 1000
        else:
            mylist[i][j]=int(mylist[i][j])

track = []
pre_per = per([1, 2, 3, 4, 5, 6, 7, 8])
for oneTrack in pre_per:
    track.append(list(oneTrack))

for i in range(len(track)):
    track[i].append(9)
    track[i].insert(0,0)

min_track =10000
cost_track = 0
index_track = []

for oneTrack in track:
    for i in range(9):
        cost_track+=mylist[oneTrack[i]][oneTrack[i+1]]
    if(cost_track<= min_track):
        min_track = cost_track
        index_track = oneTrack
    cost_track=0
        
print("the lowest cost track is: " + str(min_track)+ "\nroute = " +str(index_track))
