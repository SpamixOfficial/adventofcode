file = open("input1.txt").read()
lines = file.splitlines()
tempstr = ""
numindex = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

finalnum = 0

for line in lines:
    index = 0
    for character in line: 
        try:
            int(character)
            tempstr += character
        except:
            for num in numindex:
                if line[index:index+len(num)] == num:
                    tempstr += numindex[num]  
        index += 1
    firstnum = tempstr[0]
    lastnum = tempstr[len(tempstr)-1]
    finalnum += int((firstnum + lastnum))
    print(f"String: {line}, tempstr: {tempstr}, finalnum: {firstnum + lastnum}")
    tempstr = ""
print(finalnum)
