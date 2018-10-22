# Return true if line segments (x1, y1)->(x2, y2) and (x3, y3)->(x4, y4)
# intersect.
def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    denom = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
    if denom == 0:
        return False
    x = (((y1 - y3) * (x4 - x3)) - ((x1 - x3) * (y4 - y3))) / denom
    y = (((y1 - y3) * (x2 - x1)) - ((x1 - x3) * (y2 - y1))) / denom
    return (x >= 0 and x <= 1) and (y >= 0 and y <= 1)
