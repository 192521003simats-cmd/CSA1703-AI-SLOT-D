rooms = {'A': 'Dirty', 'B': 'Dirty'}

for location in ['A', 'B']:
    if rooms[location] == 'Dirty':
        print('Room', location, 'is Dirty. Action: Clean')
        rooms[location] = 'Clean'
    else:
        print('Room', location, 'is Clean.')

print('Final Status of Rooms:', rooms)
