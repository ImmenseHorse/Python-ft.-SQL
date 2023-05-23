with open("Products.csv", "r", encoding="UTF-8") as prod:
    things = prod.readlines()
    for i in range(len(things)):
        things[i] = things[i].rsplit(",")

        things[i][-1] = things[i][-1].strip()

    sellP = []
    for j in range(1, len(things)):
        sellP.append(float(things[j][-1]))

    sellDup = sellP.copy()

    indices = []

    for k in range(5):
        val = min(sellDup)
        pos = sellP.index(val)

        indices.append(pos)
        sellDup.remove(val)
        sellP[pos] = "*"

    print("\nThe 5 lowest-priced products are:")
    for a in indices:
        print(things[a + 1][1])
