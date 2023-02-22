rgb_hex_dict = {x: str(x) if x < 10 else chr(x + 55) for x in range(16)}


def rgb(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    r_hex = f"{rgb_hex_dict[r // 16]}{rgb_hex_dict[r % 16]}"
    g_hex = f"{rgb_hex_dict[g // 16]}{rgb_hex_dict[g % 16]}"
    b_hex = f"{rgb_hex_dict[b // 16]}{rgb_hex_dict[b % 16]}"
    return f"{r_hex}{g_hex}{b_hex}"


print(rgb(0, 1, 1))