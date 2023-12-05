lines = open("input.txt").read().splitlines()
height = len(lines)
width = len(lines[0])
xindex = 0
yindex = 0
cnum = ""
broken = False
tempstr = ""
finalnum = 0
nums = []
tempout = ""
found = False
for line in lines:
    for character in line: 
        if character.isdigit():
            if not found:
                for y in range(-1, 2):
                    if not yindex+y > 139:
                        for x in range (-1, 2): 
                            if not xindex+x > 128:
                                if not lines[yindex+y][xindex+x].isdigit() and lines[yindex+y][xindex+x] != ".":
                                    tempstr += character
                                    found = True
            else:
                tempstr += character
        else: 
            found = False
            if tempstr != "":
                nums.append(tempstr)
                finalnum += int(tempstr)
                tempstr = ""
                    
        xindex += 1
    xindex = 0
    yindex += 1
#tempnum = 0
#for value in nums:
#    tempnum += int(value)
print(finalnum)
#print(nums)
