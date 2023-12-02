from numpy import*
from plotting import plot_transformation
import math
def transformations(x,y,k,theta):
    xy=tuple(zip(x,y))
    xy1=list(zip(x,y))
    print(xy)
    theta=math.radians(theta)
    

    #Shear Shape
    shear_matrix=array([[1,k],[0,1]])
    ab=[]
    for i in xy1:
        x=shear_matrix@i
        print(x)
        ab.append(x)
    print(ab)
    #Original points
    point_1=xy[0]
    point_2=xy[1]
    point_3=xy[2]
    point_4=xy[3]
    #New Points
    xy_shear_point_1=tuple(shear_matrix@point_1)
    xy_shear_point_2=tuple(shear_matrix@point_2)
    xy_shear_point_3=tuple(shear_matrix@point_3)
    xy_shear_point_4=tuple(shear_matrix@point_4)
    xy_shear=[xy_shear_point_1,xy_shear_point_2,xy_shear_point_3,xy_shear_point_4]
    #xy_shear=tuple(new_coordinates)
    #plot_transformation(xy,xy_shear)
    print(xy_shear)
    
    #Rotate Shape
    rotate_matrix=array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
    print(rotate_matrix)
    #New Points
    xy_rotate_point_1=tuple(rotate_matrix@point_1)
    xy_rotate_point_2=tuple(rotate_matrix@point_2)
    xy_rotate_point_3=tuple(rotate_matrix@point_3)
    xy_rotate_point_4=tuple(rotate_matrix@point_4)
    xy_rotate=[xy_rotate_point_1,xy_rotate_point_2,xy_rotate_point_3,xy_rotate_point_4]
    #print(new_coordinates_1)
    return xy_shear,xy1,xy_rotate
x=transformations([1,4,4,1],[1,1,4,4],1.1,45)
xy_shear=x[0]
xy=x[1]
xy_rotate=x[2]

plot_transformation(xy,xy_shear)
plot_transformation(xy,xy_rotate)



