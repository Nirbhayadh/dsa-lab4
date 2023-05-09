# box=[]
# size=20
# class Object:
#     def __init__(self, name, profit, weight):
#         self.name = name
#         self.profit=profit
#         self.weight= weight
# # obj0= Object("Object0", 0,0)
# # obj1= Object("Object1", 1,2)
# # obj2= Object("Object2", 2,3)
# # obj3= Object("Object3", 5,4)
# # obj4= Object("Object4", 6,5)

# obj0= Object("Object0", 0,0)
# obj1= Object("Object1", 25,18)
# obj2= Object("Object2", 24,15)
# obj3= Object("Object3", 15,10)

# box.append(obj0)
# box.append(obj1)
# box.append(obj2)
# box.append(obj3)
# box.append(obj4)
def dynamic(box,size):
    rows, cols = (len(box), size+1)
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]


    for i in range(rows):
        if i == 0:
            continue
        for j in range(cols):
            if j==0:
                continue
            if box[i].weight <= j:

                matrix[i][j]= max(matrix[i-1][j], matrix[i-1][j- box[i].weight]+box[i].profit)
            else:
                matrix[i][j]=matrix[i-1][j]
    sp=[]
    j=cols-1
    i=rows-1
    while i>0 and j>0:

        if matrix[i][j]!=matrix[i-1][j]:
            sp.append({"name":box[i].name, "profit":box[i].profit})
            j=j-box[i].weight
        i=i-1
    return (sp,matrix[rows-1][cols-1])
  


# print("*******************")
# output=dynamic(box)
# print(output)

