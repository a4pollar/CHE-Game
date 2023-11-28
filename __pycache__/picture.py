#Alexa Pollard (21075914)

import numpy as np

def create_picture_frame(width,height,char):
    if type(width) != int or type(height) != int or type(char) != str or char not in "[@_!#$%^&*()<>?/|}{~:]" or height<3 or width<3:
        print("Invalid")
        return None
    y=np.full((height,width),char)
    (m,n)=y.shape
    for i in range(len(y)):
        for j in range(len(y[i])):
            if 0<i<height-1  and 0<j<width-1:
                y[i,j]=" "
    return y


def print_picture_frame(create_picture_frame):
    if create_picture_frame is None:
        return None
    for _ in create_picture_frame:
        for i in _:
            print(i,end="")
        print()

if __name__=="__main__":
    print_picture_frame(create_picture_frame(4,5,'?'))