import sys
# for using matrix
import numpy
from pygame import surfarray
# for the graphical interface
import pygame
from pygame.locals import *




#function for display your bitmap that take a matrix as a parameter
def surfdemo_show(array_img):
    "displays a surface, waits for user to continue"
    screen = pygame.display.set_mode((500,500), 0)
    # we multiply by 255 beacause python do not use manachrmatic bitmap format
    copieColorArray = array_img*255
    surface = surfarray.make_surface(copieColorArray)
    # we scale up the image (16*16 is realy small)
    surface = pygame.transform.scale(surface, (500,500))
    # we display
    screen.blit(surface,(0,0))
    pygame.display.flip()
    pygame.display.set_caption("Clic to continue.")
    # we continue until we clic or quit
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == (pygame.MOUSEBUTTONDOWN or QUIT):
                continuer = False
    pygame.quit()


# function to convert a normal matrix into a LIL (list of list) format
def LIL(a):
    # creation of the matrix that take the result
    resultMatrix = []
    # passing through the rows
    for row in range(numpy.size(a,1)):
        # passing through the columns
        for column in range(numpy.size(a,0)):
            # when we found a not zero value...
            if (a[row][column] != 0):
                # update the result matrix with the coordinate and value of each elements
                resultMatrix.append([row, column, a[row][column]])
    # we return the result matrix
    return numpy.array(resultMatrix)
    

# function to convert a normal matrix into a CSR (Compressed Spares Rows) format
def CSR(a):
    # creation of the different arrays that take the diferrent data
    value = []
    columnArr = []
    rowptr = []
    # passing through the rows
    for row in range(numpy.size(a,1)):
        # we re asigne this value at each new line
        firstOfRow = False
        # passing through the columns
        for column in range(numpy.size(a,0)):
            # when we found a not zero value...
            if (a[row][column] != 0):
                # we update the value array
                value.append(a[row][column])
                # same for the column array
                columnArr.append(column)
                # We see if it's the first time that we see a non-zero value in a line
                if firstOfRow == False:
                    # we update the row ptr array with the idex of the current value in the value array
                    rowptr.append(len(value)-1)
                    # we update this value to 
                    firstOfRow = True
    # we return the three arrays
    return (value, columnArr, rowptr)



print("\nThis program converts a normaly displayed sparse matrix from a picture or a txt to a LIL or Yale format")
print("These formats take up less storage and allows to do faster operations.")
answer = int(input("Please enter 1 or 2 to choose your array :   1.Simple exemple    2.A pixel cat picture\n"))
while (answer not in [1, 2]):
    answer = int(input("Error you didn't enter 1 or 2.\nPlease re-enter 1 or 2 to choose your array :   1.Simple exemple    2.A pixel cat picture\n"))
    
# Condition depending on the choice of the user
if (answer == 1):
    a = numpy.array([[1,0,2],[2,1,0],[0,1,3]])
    
elif (answer == 2):
    # implementing the picture of the cat (bitmap format) into the program
    imgsurface = pygame.image.load('cat.bmp')
    # creation of a matrix that contain the value of each pixel
    imgarray = surfarray.array2d(imgsurface)
    a = numpy.array(imgarray)
    # we display the image in a window
    surfdemo_show(a)
    # we display the corresponding matrix in the console
    a = numpy.array(imgarray)
    print(a)

answer = int(input("Please enter 1 or 2 to choose your format :   1.LIL (LIst of List)    2.CSR (Compressed Sparse Row)\n"))
while (answer not in [1, 2]):
    answer = int(input("Error you didn't enter 1 or 2.\nPlease enter 1 or 2 to choose your format :   1.LIL (LIst of List)    2.CSR (Compressed Sparse Row)\n"))
# We print the the result if the choice is LIL
if (answer == 1):
    result = LIL(a)
    print(result)
# We print the the result if the choice is CSR
elif (answer == 2):
    value, columnArr, rowptr = CSR(a)
    print("value  :",value) 
    print("\ncolumn :",columnArr) 
    print("\nrowptr :",rowptr)