
if __name__ == '__main__':
    str_height, str_width = input().split()
    height, width = int(str_height), int(str_width)
    rows = height // 2
    symbol = ".|."
    for x in range(rows):
        dashes = (width - len(symbol)) / 2
        dash = "-" * int(dashes)
        print(f"{dash}{symbol}{dash}")
        if x != rows - 1:
            symbol += ".|..|."

    mid = int((width - 7) / 2)
    mid_str = ""
    for x in range(0, mid):
        mid_str += "-"
    print(f"{mid_str}WELCOME{mid_str}")

    for x in range(rows):
        dashes = (width - len(symbol)) / 2
        dash = "-" * int(dashes)
        print(f"{dash}{symbol}{dash}")
        symbol = symbol.replace(".|.", "", 2)

