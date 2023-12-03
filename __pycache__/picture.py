#Alexa Pollard (21075914)

import numpy as np

def create_picture_frame(width,height,char):
    if type(width) != int or type(height) != int or type(char) != str or len(char)!=1 or height<3 or width<3:
        print("invalid!")
        return None
    picture_frame=np.full((height,width),char)
    (m,n)=picture_frame.shape
    for i in range(1,m-1):
        for j in range(1,n-1):
            picture_frame[i,j]=" "
    return picture_frame


def print_picture_frame(create_picture_frame):
    if create_picture_frame is None:
        return None
    for row in create_picture_frame:
        for i in row:
            print(i,end="")
        print()

if __name__=="__main__":
    print_picture_frame(create_picture_frame(2,5,'O'))