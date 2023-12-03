from numpy import*
from plotting import plot_transformation
import math
def transformations(x,y,k,theta):
    if theta!=int or k!=int or len(x) != len(y):
        return None
    theta=math.radians(theta)
    xy=tuple(zip(x,y))
    shear_matrix=array([[1,k],[0,1]])
    rotate_matrix=array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
    xy_shear=[]
    xy_rotate=[]

    for coordinate in xy:
        shear_point=tuple(shear_matrix@coordinate)
        xy_shear.append(shear_point)

    for coordinate in xy:
        rotate_point=tuple(rotate_matrix@coordinate)
        xy_rotate.append(rotate_point)

    return xy_shear,xy,xy_rotate

if __name__=='__main__':
    transformation_values=transformations([1,4,4,1],[1,1,4,4],1.1,45)
    xy_shear=transformation_values[0]
    xy=list(transformation_values[1])
    xy_rotate=transformation_values[2]
    plot_transformation(xy,xy_shear)
    plot_transformation(xy,xy_rotate)