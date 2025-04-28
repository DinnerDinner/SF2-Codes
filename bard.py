# '''
# Bard:

# Every evening villagers in a small village gather around a big fire and sing songs.

# A prominent member of the community is the bard. Every evening if the bard is present, he sings a brand new song that no villager has heard before, and no other song is sung that night. In the event that the bard isnt present, other villagers sing without him and exchange all songs that they know. (NOTE: villagers can only learn new songs from the bard)

# Given the list of villagers present for E consecutive evenings, output all villagers that know all songs sung during that period.

# INPUT:

#     first line is an integer N, number of villagers

#     2nd line is an integer E, number of evenings

#     next E lines contain the list of villagers present on each of the E evenings. Each line begins with a positive integer K, the number of villagers present during that evening followed by K integers seperated by spaces representing the villagers.

#     No villager will appear twice in one night and the bard will appear at least once across all nights. Villager number 1 is the bard

# OUTPUT: 

#     all villagers that know all songs, including the vard, one integer per line in ascending order
# logan carried by actually noting it down


# '''



n = int(input())  
e = int(input())  
villager_songs = {i: set() for i in range(1, n + 1)}  
song_id = 1  

for i in range(e):
    data = list(map(int, input().split()))
    villagers_present = set(data[1:])
    
    if 1 in villagers_present: 
        for villager in villagers_present:
            villager_songs[villager].add(song_id)
        song_id += 1
        
    else: 
        shared_songs = set()
        for villager in villagers_present:
            shared_songs.update(villager_songs[villager])

        for villager in villagers_present:
            villager_songs[villager].update(shared_songs)


result = [villager for villager, known_songs in villager_songs.items() if known_songs == villager_songs[1]]
for villager in sorted(result):
    print(villager)
