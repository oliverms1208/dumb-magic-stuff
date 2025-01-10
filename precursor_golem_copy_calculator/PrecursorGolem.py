
# Returns the number of precursor golems and non-precursor golems 
# after casting a copy spell, including the originals.

# This is wrong btw
def precursor_golem(precursors: int, golems: int, copies: int = 1) -> tuple[int, int]:
    if golems == 0:
        new_precursors = copies + (copies * precursors) * (precursors - 1)
        new_golems = new_precursors * 2
    else:
        # Assuming you target a non-precursor with the copy spell
        new_precursors = copies * precursors * precursors
        new_golems = new_precursors * 2 + copies + (copies * precursors) * (golems - 1)
    if copies == 1:
        return (precursors + new_precursors, golems + new_golems)
    else:
        return precursor_golem(precursors + new_precursors, golems + new_golems, copies - 1)

print(precursor_golem(1, 2, 5))
print(precursor_golem(6, 22, 5))