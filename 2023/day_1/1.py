file = open("input1.txt").read()
lines = file.splitlines()
tempstr = ""
finalnum = 0
for line in lines:
    for character in line:
        try:
            int(character)
            tempstr += character
        except:
            continue
    firstnum = tempstr[0]
    lastnum = tempstr[(len(tempstr) - 1)]
    finalnum += int(firstnum+lastnum)
    print(f"String: {line}, tempstr: {tempstr}, first: {firstnum}, last: {lastnum}, num: {firstnum+lastnum}")
    tempstr = ""

print(finalnum)
