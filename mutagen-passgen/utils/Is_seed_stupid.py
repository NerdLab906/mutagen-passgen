from datetime import datetime
import json


def rebuilder():
    seeds = [
        "849173620",
        "967314285",
        "731895406"
    ]

    time = datetime.now().hour
    if 5 <= time < 12:
        current = seeds[0]
        now = "morning"
    elif 12 <= time < 17:
        current = seeds[1]
        now = "day"
    elif 17 <= time < 22:
        current = seeds[2]
        now = "evening"
    else:
        current = seeds[2][::-1]
        now = "night"

    with open("data/FR.json", "r") as file:
        subtract = json.load(file)

    chars = list(current)
    for i in range(len(chars)):
        a = int(chars[i])

         # RANGE < 4 
        if 0 < a < 4 and now == "morning":
            a = ((a + 1) * (subtract["counter"] + 2)) % 10
            chars[i] = str(a)
        elif 0 < a < 4 and now == "day":
            a = (a + 2) % 10
            chars[i] = str(a)
        elif 0 < a < 4 and now == "night":
            a = (a * 3 + subtract["counter"]) % 10
            chars[i] = str(a)

        # RANGE > 4    
        elif 4 < a < 9 and now == "morning":
            a = (a ^ subtract["counter"]) % 10
            chars[i] = str(a)
        elif 4 < a < 9 and now == "day":
            a = (a + subtract["counter"] + i) % 10
            chars[i] = str(a)
        elif 4 < a < 9 and now == "evening":
            if a % 2 == 0:
                a = 9 - a
            else:
                a = a ^ 3
            chars[i] = str(a)

    checksum = sum(int(ch) for ch in chars) % 10
    chars.insert(checksum, str(3))

    subtract["counter"] = (subtract["counter"] + 1) % 4
    with open("data/FR.json", "w") as file:
        json.dump(subtract, file, indent=4)

    return ''.join(chars)
