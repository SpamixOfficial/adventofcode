lines = open("input.txt").read().splitlines()
index = 0
colors = ["green", "blue", "red"]
powersum = 0

for line in lines:
    values = line.replace(":", ";").replace(",", ";").split(";")
    values.pop(0)
    highest = {
        "green": 0,
        "blue": 0,
        "red": 0
    }
    for value in values:
        num = int(value[:3].strip())
        color = ""
        for color in colors:
            if color in value:
                break
        if highest[color] < num:
            highest[color] = num
    powersum += highest["green"] * highest["red"] * highest["blue"]

print(powersum)
