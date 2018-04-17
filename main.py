# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# from matplotlib import image as mpimg
# import checklines
#
# img = cv2.imread('example.jpg')
# checklines.checkLines(img)
#


import cv2
from matplotlib import pyplot as plt
import checklines as cl
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('test3.jpg')

newImg = np.float64(img)
res=cl.ContLines(newImg)
res=np.uint8(res)

img2 = cv2.imread('testt.jpg')
newImg2 = np.float64(img2)
res2=cl.ContLines(newImg2)
res2=np.uint8(res2)


plt.figure()

plt.subplot(121)
plt.title("Original Img")
plt.axis("off")
plt.imshow(img[:, :, ::-1])

plt.subplot(122)
plt.title("Continuous Lines Image")
plt.axis("off")
plt.imshow(res[:, :, ::-1])

plt.show()



plt.figure()

plt.subplot(121)
plt.title("Original Img")
plt.axis("off")
plt.imshow(img2[:, :, ::-1])

plt.subplot(122)
plt.title("Continuous Lines Image")
plt.axis("off")
plt.imshow(res2[:, :, ::-1])

plt.show()



