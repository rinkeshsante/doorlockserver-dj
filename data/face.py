def makeFacePoints(image):
    ls = [i for i in image]
    return ls[:5]


def compareFacePoinst(l1, l2):
    val = 0
    for i, j in zip(l1, l2):
        if i - j <= (i+j)/20:
            val += 1

    return val / len(l1)
