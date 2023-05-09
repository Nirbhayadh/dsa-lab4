# box=[]
# size=20
# class Object:
#     def __init__(self, name, profit, weight):
#         self.name = name
#         self.profit=profit
#         self.weight= weight
#         self.pr=round(profit/weight,2)   

# obj1= Object("Object1", 25,18)
# obj2= Object("Object2", 24,15)
# obj3= Object("Object3", 15,10)

# box.append(obj1)
# box.append(obj2)
# box.append(obj3)

# for i in box:
#     print(i.name, i.profit, i.weight)

def greedy(box, size):
    profit=0
    box.sort(key= lambda x: x.pr, reverse= True)
    sp=[]
    obj=None
    for i in box:
        if size<=0:
            break
        if i.weight<=size:
            profit=profit + i.profit
            size=size-i.weight
            obj={"name":i.name,"profit":i.profit}
            # obj=Object(i.name, i.profit, i.weight)
        else:
            profit= profit + i.profit * (size/i.weight)
            # obj=Object(i.name, i.profit * (size/i.weight), round(size/ i.weight,2) )
            obj={"name":i.name,"profit":i.profit * (size/i.weight)}
            
            size=0
        sp.append(obj)
    return (sp,profit)
        

# print("*******************")
# (x,profit)=greedy(box,size)
# print(x,profit)




