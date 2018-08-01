class Root:  # root of a tree
    def __init__(self, ppl, can, bank):
        self.bank = bank
        self.ppl = ppl
        self.can = can


class Node:  # nodes of a tree
    def __init__(self, ppl, can, bank, parent, isfinal=None):
        self.bank = bank
        self.ppl = ppl
        self.can = can
        self.parent = parent
        self.isFinal = isfinal


class Tree: # tree itself keeps root and nodes
    def __init__(self, root):
        nodes = []
        self.root = root
        self.nodes = nodes


main = Root(3, 3, "left")  # main - current node
tree = Tree(main)
nodeCount = 0
flag = True

while flag:
    currBank = main.bank
    if currBank == "left":  # there are 3 operations for crossing from the left bank: send 2 cann, send 2 miss and a cann
                            # and just 2 miss
        nodeArr = [Node(main.ppl, main.can, "right", main, None) for j in range(3)]

        nodeArr[0].ppl -= 2

        nodeArr[1].can -= 2

        nodeArr[2].ppl -= 1
        nodeArr[2].can -= 1

        for i in range(3):  # checks if operations give a negative result 
                            # if node satisfies comndition that there a more miss than cann - then it is picked to be current
                            # if node's quantity of miss and cann equals zero then it's final
            if nodeArr[i].ppl < 0 or nodeArr[i].can < 0:
                continue

            if nodeArr[i].ppl >= nodeArr[i].can and 3-nodeArr[i].ppl >= 3-nodeArr[i].can or nodeArr[i].ppl == 0 \
                    or 3-nodeArr[i].ppl == 0:
                tree.nodes.append(nodeArr[i])

            if nodeArr[i].ppl == 0 and nodeArr[i].can == 0:
                nodeArr[i].isFinal = True
                flag = False

        if tree.nodes[nodeCount].isFinal:   # checks if final
            while tree.nodes[nodeCount].isFinal:
                nodeCount += 1
        else:
            main = tree.nodes[nodeCount]  # picks another node as a current
            nodeCount += 1

    if currBank == "right":  # there are two options for right bank: send cann or send cann and miss
                                
        nodeArr = [Node(main.ppl, main.can, "left", main, None) for j in range(3)]

        nodeArr[0].can += 1

        nodeArr[1].ppl += 1

        if nodeArr[2].ppl <= 1 and nodeArr[2].can <= 1:
            nodeArr[2].ppl += 1
            nodeArr[2].can += 1
        else:
            nodeArr[2].ppl += 10

        for i in range(3):
            if nodeArr[i].ppl > 3 or nodeArr[i].can > 3:
                continue
            if nodeArr[i].ppl >= nodeArr[i].can and 3 - nodeArr[i].ppl >= 3 - nodeArr[i].can or nodeArr[i].ppl == 0 \
                    or 3 - nodeArr[i].ppl == 0:
                tree.nodes.append(nodeArr[i])
            if nodeArr[i].ppl == 0 and nodeArr[i].can == 0:
                    nodeArr[i].isFinal = True
                    flag = False

        if tree.nodes[nodeCount].isFinal:
            while tree.nodes[nodeCount].isFinal:
                nodeCount += 1
        else:
            main = tree.nodes[nodeCount]
            nodeCount += 1

for i in tree.nodes:  # prints result
    count = 0
    if i.isFinal:
        result = []
        while i != tree.root:
            result.append(i.bank)
            result.append(i.can)
            result.append(i.ppl)
           # print(i.ppl, i.can, i.bank)
            i = i.parent
            count += 1
            bank = ""
        for j in range(len(result)-1, 0, -3):
            if result[j-2] == "right":
                bank = "right"
            if result[j-2] == "left":
                bank = "left"
            ppl = 3 - result[j]
            can = 3 - result[j-1]
            print("From ", bank, " bank ", ppl, " missionaries and ", can, " cannibals.")
        print("found solution in ", count, "steps")
        print(result)
