from utils.Is_seed_stupid import rebuilder
from core.Entropy import entropy
from collections import Counter
from datetime import datetime 
import json


def mutation(seed):
    formula = {
        "0": (int(seed[1]) + len(seed)) % 17,
        "1": (int(seed[-2]) * 2 + int(seed[0])) % 20,
        "2": (sum(int(c) for c in seed) + int(seed[-1])) % 25,
        "3": (abs(int(seed[0]) - int(seed[1])) + 3) % 15,
        "4": (int(seed[2]) * int(seed[3]) + 7) % 30,
        "5": (int(seed[4]) + int(seed[5]) + int(seed[-3])) % 22,
        "6": ((int(seed[3]) + int(seed[-2])) ** 2) % 50,
        "7": ((int(seed[0]) ^ int(seed[-1])) + len(set(seed))) % 33,
        "8": (int(seed[6]) + int(seed[-4])) % 12,
        "9": ((int(seed[1]) + 1) * (int(seed[2]) + 1)) % 18
    }   

    mutated_seed = []
    for char in seed:
        if char in formula:
            mutated_seed.append(str(formula[char]))
    return "".join(mutated_seed)

#AFTER FROM MUTATE THIS FUNCTION GAVES US NEW RANDOMIZED PASSWORD, ALMOST RANDOMIZED 
def password_generator(seed, style):
    c = Counter(seed)
    commons = c.most_common(2)
    if sum(count for _, count in commons) > 3:
        value = rebuilder()
    else:
        seed = entropy(seed)
        value = mutation(seed)
    seed = value 
    styles = [
        ["%#", "$^", "/*T", "@!", "=)L", "[Q", "`Y", ":A", "!R" ,"|M"],
        ["⸮Ꙭ", "※☍", "⁂", "❆✴", "☍⁖", "☄☢", "✴⚚", "⚛⚗", "☣⋆" ,"Ꙭ⁂"],
        ["☉☼", "♆⚶", "☠✠", "♁♆", "☍⁖", "☼☽", "✬✮", "✩✪", "✡✦" ,"☠✠"]
    ]

    rare = ["±", "§", "Z", "~", "¶", "¿"]
    second = datetime.now().second
    index1 = (second // 10) % len(rare)
    index2 = (second // 7 + index1) % len(rare)
    symbol1 = rare[index1]
    symbol2 = rare[index2]
    if index1 == index2:
        index2 = (index2 + 1) % len(rare)


    symbols = {}
    if style == "classic" or style is None:
        for num, char in enumerate(styles[0]):
            symbols[str(num)] = char
    elif style == "chaos":
        for num, char in enumerate(styles[1]):
            symbols[str(num)] = char
    elif style == "mystic":
        for num, char in enumerate(styles[2]):
            symbols[str(num)] = char        


    password = []
    for char in seed:
        if char in symbols:
            password.append(symbols[char])
    
    improved_password = []
    for c in password:
        if c not in improved_password:
            improved_password.append(str(c))
    
    arr_index1 = (second // 6) % len(improved_password)
    arr_index2 = (second // 8) % len(improved_password)
    if arr_index1 == arr_index2:
        arr_index2 = (arr_index2 + 1) % len(improved_password)

    improved_password.insert(arr_index1, symbol1)
    improved_password.insert(arr_index2, symbol2)
    return "".join(improved_password)[:16]