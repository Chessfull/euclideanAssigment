import random #Imported for creating random points

#1-Create a list that includes 2D points like (x,y) in tuples
points=[]
try:
    numberPoints=int(input("How many points you want add in this list?"))
except:
    print("Please write a integer")
    numberPoints=int(input("How many points you want add in this list?"))
for i in range(numberPoints):
    x1=random.randint(1,100)
    y1=random.randint(1,100)
    points.append((x1,y1))
print(points)

#2-Define function ‘euclideanDistance’ that calculated euclidean distance between two 2D points
def euclideanDistance(userPoint1,userPoint2):
    x1,y1=userPoint1
    x2,y2=userPoint2
    return (((x2-x1)**2)+((y2-y1)**2))*0.5

#3-Use loop for calculation each point euclidean distance in 'points' that you create and add these as new list named 'distances'
distances=[]
for x_ in range(len(points)):
    for y_ in range(len(points)):
        if x_==y_:
            break
        eachPointCalculation=euclideanDistance(points[x_],points[y_])
        distances.append(eachPointCalculation)
print(distances)

#4-Find minimum distance in 'distances' list
minDistance=[]
for i in distances:
    minDistance.append(i)
print(min(minDistance))







