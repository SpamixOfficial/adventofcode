lines = open("input.txt").read().splitlines()
index = 0
colors = {"green": 13, "blue": 14, "red": 12}
posgames = 0

for line in lines:
    possible = True
    index += 1
    values = line.replace(":", ";").replace(",", ";").split(";")
    values.pop(0)
    for value in values:
        num = int(value[:3].strip())
        color = ""
        for color in colors:
            if color in value:
                break
        print(num)
        print(colors[color])
        print(num > colors[color])
        print("--")
        if num > colors[color]:
            possible = False
            break
    if possible:
        posgames += index

print(posgames)
