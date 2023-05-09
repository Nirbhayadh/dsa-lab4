# box=[]

# size=20
# profit=0
# class Object:
#     def __init__(self, name, profit, weight):
#         self.name = name
#         self.profit=profit
#         self.weight= weight

    

# obj1= Object("Object1", 25,18)
# obj2= Object("Object2", 24,15)
# obj3= Object("Object3", 15,10)

# box.append(obj1)
# box.append(obj2)
# box.append(obj3)

# for i in box:
#     print(i.name, i.profit, i.weight)


def knapSackFractional(n, box, size, i):
    
    if i==n or size<=0:
        return 0   

    if box[i].weight<=size:
        profitin= box[i].profit + knapSackFractional(len(box), box, size-box[i].weight, i+1)
        profitout= knapSackFractional(len(box), box, size, i+1)
    else:
        profitin= box[i].profit *  (size / box[i].weight)
        profitout= knapSackFractional(len(box), box, size, i+1)
    return max(profitin, profitout)
    
def knapSack01(n, box, size, i):
    
    if i==n or size<=0:
        return 0   

    if box[i].weight<=size:
        profitin= box[i].profit + knapSack01(len(box), box, size-box[i].weight, i+1)
        profitout= knapSack01(len(box), box, size, i+1)
        return max(profitin, profitout)
    else:
        profitout= knapSack01(len(box), box, size, i+1)
        return profitout


# fr=knapSackFractional(len(box), box, size, 0)
# zerone=knapSack01(len(box), box, size, 0)
# print(fr)
# print(zerone)

# for i in sp:
#     print(i)





