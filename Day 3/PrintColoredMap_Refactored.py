# ---- Data responsibility ----
def get_major_colors():
    return ["White", "Red", "Black", "Yellow", "Violet"]

def get_minor_colors():
    return ["Blue", "Orange", "Green", "Brown", "Slate"]

# ---- Core logic depends on Abstraction of Print Functionality ----
def print_color_map(printer):
    major_colors = get_major_colors()
    minor_colors = get_minor_colors()

    pair_number = 0
    for major in major_colors:
        for minor in minor_colors:
            printer(pair_number, major, minor)
            pair_number += 1

    return pair_number