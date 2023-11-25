l=[2,3,4,5,6,7]
def linear_search(l,item,issorted=False):
    if(type(l)==list and type(item)==int or type(item)==float and type(issorted)==bool):
        for i in range(len(l)):
            if l[i]==item:
                return i
        return None
    else:
        print("Invalid Input")
        return None
    
def binary_search(l,item,issorted=False):
    if(type(l)==list and type(item)==int or type(item)==float and type(issorted)==bool):
        if issorted==False:
            return linear_search(l,item,issorted=False)
        if issorted==True:
            i=0
            j=len(l)-1
            while i <=j:
                m=(i+j)//2
                if l[m]==item:
                    return m
                elif l[m]<item:
                    i=m+1
                else:
                    j=m-1
            return None
    else:
        print("Invalid Input")
        return None

    