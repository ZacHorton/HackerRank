def lowestTriangle(trianglebase, area):
    height = int(math.ceil(area / trianglebase * 2))
    if height <= 0:
        return 1
    else:
        return height
