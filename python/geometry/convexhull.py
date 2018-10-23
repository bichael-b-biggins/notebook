## With inspiration from https://github.com/INSAlgo/ICPC-Notebook

def convex_hull(points):
    # Dedupe & sort lexicographically.
    points = sorted(set(points))

    # Boring case. No points, or a single point, maybe repeated.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross
    # product.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in points[::-1]:
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concat lower and upper hulls.
    # Last point of each is omitted as it is repeated at the beginning of the
    # other list.
    return lower[:-1] + upper[:-1]
