import random as rand

types = ["land", "creature", "enchantment", "artifact", "instant", "sorcery"]
colours = ["colourless", "white", "blue", "black", "red", "green", "multicolour"]
min_mv = 1
max_mv = 5

type = rand.choice(types)
if type == "land":
    print(f"The joker is a land.")
else:
    print(f"The joker is a {rand.choice(colours)} {type} with mana value equal to {rand.randint(min_mv, max_mv)}.")