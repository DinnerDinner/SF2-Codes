def covers(platform, horizontal_pos):
    '''
    :param platform: a platform as defined by the input of the question
    :param horizonal_pos: an integer
    :return : True if platform covers horizontal_post; False otherwise. 
    '''
    return platform[1]+0.5 <= horizontal_pos <= platform[2]-0.5


def pillar_from(platforms, height, horizontal_pos, horizontal_pos2):
    '''
    :param platforms: a list of platforms (as lists)
    :param height: vertical position
    :param horizontal_pos: horizontal position
    :return : minimum length of pillar from heigh and horizontal_pos to the platform/ground below
    '''


    bottom = 0
    for platform in platforms:
        if (platform[0] < height and covers(platform, horizontal_pos)):
            bottom = max(bottom, platform[0])
    a = (height-bottom)

    bottom2 = 0
    for platform in platforms:
        if (platform[0] < height and covers(platform, horizontal_pos2)):
            bottom2 = max(bottom2, platform[0])
    b = (height-bottom2)

    return a+b


n = int(input())

platforms = []

# read input from user as lists of integers
for i in range(n):
    platform = input().split()
    platforms.append(platform)
    for j in range(len(platform)):
        platform[j] = int(platform[j])

print(platforms)

total = 0

for platform in platforms:    
    total += pillar_from(platforms, platform[0], platform[1], platform[2])
    

print(total)
