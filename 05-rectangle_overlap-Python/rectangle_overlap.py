# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 

import math
def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    i1,j1=left1,top1
    i2,j2=left1+width1,top1
    i3,j3=left1+width1,top1+height1
    i4,j4=left1,top1+height1
    k1,l1=left2,top2
    k2,l2=left2+width2,top2
    k3,l3=left2+width2,top2+height2
    k4,l4=left2,top2+height2
   

    if(i1,j1==k1,l1) or (i1,j1==k2,l2) or (i1,j1==k3,l3) or (i1,j1==k4,l4):
        return True
    elif(i2,j2==k1,l1) or (i2,j2==k2,l2) or (i2,j2==k3,l3) or (i2,j2==k4,l4):
        return True
    elif(i3,j3==k1,l1) or (i3,j3==k2,l2) or (i3,j3==k3,l3) or (i3,j3==k4,l4):
        return True
    elif(i4,j4==k1,l1) or (i4,j4==k2,l2) or (i4,j4==k3,l3) or (i4,j4==k4,l4):
        return True
    else:
        return False


   
def fun_distance(x1, y1, x2, y2):
	#by the distance formula ((x2-x1)^2 +(y2-y1)^2)^0.5
	return(int(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))))