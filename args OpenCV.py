import cv2 as cv
import numpy as np
import operator
import sys
# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (1, 1, 1), thickness = -1)
# cv.imshow('Rectangle', blank)
# cv.waitKey(0)

args = [None] * 4
for i in range(0, args.__len__()):
  try:
    args[i] = (int)(sys.argv[i + 1])
  except Exception:
    args[i] = 100
    if i == 2 or i == 3:
      args[i] = (int)((float)(args[i]) / 10)

test = np.zeros((args[0], args[1]), dtype='uint8') # Original square
offset = (args[2], args[3]) # Offsets by 16 pixels horizontally and vertically
oppos = tuple(map(operator.add, offset, test.shape)) # Get opposing corner coordinates (offset by 16 pixels)
img = np.zeros(tuple(map(operator.add, offset, oppos)), dtype='uint8') # Add a bottom-right buffer of 16 by 16 pixels

# cv.rectangle(img, (0, 0), img.shape, color=(0, 100, 0), thickness=-1)
cv.rectangle(img, offset, oppos, color=(0, 100, 0), thickness=-1)
cv.namedWindow('Rectangle', cv.WINDOW_AUTOSIZE)
cv.imshow('Rectangle', img)
cv.waitKey(0)
cv.destroyAllWindows()

#
# tuple(2, 4) + tuple(3, 6)
# = tuple(5, 10) wrong
# = tuple(2, 4, 3, 6)
# map(operation, thing1, thing2)
# for every element in thing 1, do operation on thing 2
# map(operator.add, (2, 4), (3, 6))
# returns (2 + 3, 4 + 6) = (5, 10)
#

#
# argv and argc
#
# cd ../test/
# argc (ARGument Counter): 2
# argv (ARGument Vector): ['cd', '../test']
# argv[0] == '.\learning.py'
#

# python .\learning.py 250 20
# -> size(250, 250), offset(20, 20)
# python .\learning.py 250 200 10 7
# -> size(250, 200), offset(10, 7)