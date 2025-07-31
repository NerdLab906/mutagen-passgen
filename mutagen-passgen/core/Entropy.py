import json
from datetime import datetime

def entropy(seed):
    digits = [1, 2, 3]
    minute = datetime.now().minute
    second = datetime.now().second

    with open("data/FE.json", "r") as file:
        data = json.load(file)

    chars = list(seed)
    selected_digit = digits[minute // 20]
    target_index = (second // 15) % len(seed)

    if selected_digit == 1:
        char = int(chars[target_index])
        if 0 < char < 4:
            char += data["counter"]
            chars[target_index] = str(char % 10)
        elif 4 <= char <= 7:
            char -= data["counter"]
            chars[target_index] = str(char % 10)

    elif selected_digit == 2:
        char = int(chars[target_index])
        if 0 < char < 4:
            char += data["counter"]
            chars[target_index] = str(char % 10)
        elif 4 <= char <= 7:
            if char % 2 == 0:
                char -= data["counter"]
            else:
                char += data["counter"]
            chars[target_index] = str(char % 10)

    elif selected_digit == 3:
        mid = len(seed) // 2
        left = mid - 2
        right = mid + 2 
        counter = data["counter"]

        a = int(chars[left])
        b = int(chars[right])

        # LEFT SIDE
        if 0 < a <= 4:
            d = ((a + counter + 1) * 2) % 10
            chars[left] = str(d)
        elif 5 <= a <= 9:
            if a % 2 == 0:
                d = (9 - a + counter) % 10  
            else:
                d = (a ^ (counter + left)) % 10  
            chars[left] = str(d)

        # RIGHT SIDE
        if 0 < b <= 4:
            d = ((abs(b + counter + right) * 2 + mid) % 10)
            chars[right] = str(d)
        elif 5 <= b <= 9:
            if b % 2 == 0:
                d = ((9 - b + (right % 3) + counter) % 10)
            else:
                d = ((b ^ ((left + right + mid) % 7)) % 10)
            chars[right] = str(d)

    return "".join(chars)