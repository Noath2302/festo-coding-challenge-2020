import hashlib 
import string
from itertools import permutations as per
def stringify(permutation):
    passCollection = []
    for passGroup in permutation:
        passCollection.append(''.join(passGroup))
    return passCollection
phraseKnown = [["0b","Ob","90","9O","06","O6"],["n0","nO","0u","Ou"],["6u","n9","bu"]]

code = []
for i0 in list(range(10)) + list(string.ascii_lowercase + string.ascii_uppercase):
    for i1 in list(range(10)) + list(string.ascii_lowercase + string.ascii_uppercase):
        code.append(str(i0)+str(i1))
passText_pre = []
for phrase0 in phraseKnown[0]:
    for phrase1 in phraseKnown[1]:
        for phrase2 in phraseKnown[2]:
            for phrase3 in code:
                passText_pre.extend(list(per([phrase0,phrase1,phrase2,phrase3])))

for passCode in stringify(passText_pre):
    result = hashlib.md5(passCode.encode())
    shash = result.hexdigest()
    if(shash.startswith("a84ba651fd122ef5")):
        print(passCode)
        print(shash)
