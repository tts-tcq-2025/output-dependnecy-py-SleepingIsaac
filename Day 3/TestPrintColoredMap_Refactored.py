from color_map import print_color_map

# ---- Default printer using print ----
def console_printer(pair_number, major, minor):
    print(f"{pair_number} | {major} | {minor}")

# ---- Example test printer (captures output differently) ----
def test_printer(pair_number, major, minor):
    # In real tests, you’d probably store these in a list instead of printing
    print(f"[TEST] {pair_number} - {major}/{minor}")

# ---- Usage ----
if __name__ == "__main__":
    print("Using console printer:")
    total = print_color_map(console_printer)
    print(f"Total pairs = {total}\n")

    print("Using test printer:")
    total = print_color_map(test_printer)
    print(f"Total pairs = {total}")