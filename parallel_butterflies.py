# def new_sighting(kinds, counts, sighting):
#     if sighting not in kinds:
#         kinds.append(sighting)
#         counts.append(1)
    
    
    
# kinds = ["monarch", "painted lady", "bronze copper", 'orange sulphur']
# counts = [5,2,12,7]
# new_sighting(kinds, counts, 'Common Blue')
# for i in range(len(kinds)):
#     print(f'{kinds[i]}: {counts[i]}')


d = {3: 33}
d[5]  = d.get(4, 12)
d[4] = d.get(3)
print(d)



import random
import string

def generate_codes(n=5, length=6):
    codes = []
    for _ in range(n):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        codes.append(code)
    return codes

codes = generate_codes()
print(codes)


