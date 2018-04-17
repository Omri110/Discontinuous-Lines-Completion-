

import numpy as np
import cv2

#
def case1(img,i,j,m,n):

    while (i != m and j != n):
        img[i, j] = 255
        i += 1
        j += 1
    return img

def case2(img,i,j,m,n):

    while (i != 0 and j != 0):
        img[i, j] = 255
        i -= 1
        j -= 1
    return img


def case3(img,i,j,m,n):

    while(i!=m and j!=0):
        img[i, j] = 255
        i+=1
        j-=1
    return img


def case4(img,i,j,m,n):

    while(i!=0 and j!=n):
        img[i, j] = 255
        i-=1
        j+=1
    return img



def case5(img,i,j,n):
    for j in range(0,n):
        img[i,j]=255
    # img[i,:] = (0,0,0,255)
    return img

def case6(img,i,j,m):
    for i in range(0,m):
        img[i,j]=255
    # img[:,j] = (0,0,0,255)
    return img

def case7(img,i,j,m,n):
#     for k in range(i+1, m):
#         if (img[k,j] == 255):
#             img[:, j]= 255
#
#     for l in range(j+1, n):
#         if (img[i,l] == 255):
#             img[i, :]= 255
#
#     for k in range(0, i-1):
#         if (img[k,j] == 255):
#             img[:, j]= 255
#
#     for l in range(0, j-1):
#         if (img[i,l] == 255):
#             img[i, :]= 255
    return img





def ContLines(img):
    img[img > 240] = 255
    L = img.shape

    if len(L) == 2:


        m, n = L
        newImg = np.zeros((m + 2, n + 2))
        newImg[1:m + 1, 1:n + 1] = img
        # phaseMat= np.zeros((m + 2, n + 2))

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (newImg[i, j] == 255):
                    if (newImg[i+1,j+1]==255 and newImg[i - 1, j - 1] == 255):
                        newImg=case1(newImg,i,j,m,n)
                        newImg = case2(newImg, i, j, m, n)


                    elif (newImg[i + 1, j - 1] == 255 and newImg[i - 1, j + 1] == 255):
                        newImg=case3(newImg,i,j,m,n)
                        newImg = case4(newImg, i, j, m, n)


                    elif (newImg[i, j-1] == 255 and newImg[i, j+1] == 255):
                        newImg = case5(newImg,i,j,n)

                    elif (newImg[i+1, j] == 255 and newImg[i-1, j] == 255):
                        newImg = case6(newImg,i,j,m)

                    else:
                        newImg = case7(newImg, i, j, m,n)
        return newImg
    if(len(L)==3):
        b,g,r=cv2.split(img)
        return cv2.merge((ContLines(b), ContLines(g), ContLines(r)))

#
#
# def PhaseMatrixCalculation(GradientX, GradientY):
#
#     D = (len(GradientX.shape) + len(GradientY.shape))/2
#     if D == 2:
#
#         return np.arctan2(GradientY, GradientX)
#
#     elif D == 3:
#
#         bgx, ggx, rgx = cv2.split(GradientX)
#         bgy, ggy, rgy = cv2.split(GradientY)
#
#         pmb = PhaseMatrixCalculation(bgx, bgy)
#         pmg = PhaseMatrixCalculation(ggx, ggy)
#         pmr = PhaseMatrixCalculation(rgx, rgy)
#
#         return cv2.merge((pmb, pmg, pmr))
#     else:
#         raise ValueError('Function receives only BGR, RGB or GrayScale images and both input matrices must be of identical shape')
#
# def ContLines(mat,img):
#     img = np.float64(img)
#     L = img.shape
#     if len(L) == 2:
#         m, n = L
#
#         newImg = np.zeros((m + 2, n + 2))
#
#
#
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                     if (mat[i, j] == 135):
#                         newImg[i+1,j+1]==255
#
#                     if (mat[i, j] == 45):
#                         newImg[i - 1, j - 1] == 255
#
#                     if (mat[i, j] == 225):
#                         newImg[i + 1, j - 1] == 255
#
#                     if (mat[i, j] == 315):
#                         newImg[i - 1, j + 1] == 255
#
#                     if (mat[i, j] == 180):
#                         newImg[i ,:] == 255
#
#                     if (mat[i, j] == 270):
#                         newImg[i , :] == 255
#
#                     # else:
#                     #     phaseMat[i, j] = 0
#
#         return np.uint8(newImg)
#     elif(len(L)==3):
#         b,g,r=cv2.split(img)
#         return cv2.merge((ContLines(mat,b), ContLines(mat,g), ContLines(mat,r)))
#
#     else:
#         return None
#
# def Case1(img, i, j):
#     L = img.shape
#     if (i,j== L):
#         return img
#
#     img[i, j] = 255
#     Case1(img, i+1, j+1)
#
#     else:
#
#
# def Case2(img, i, j):
#     L = img.shape
#     if (i,j==L):
#         return img
#     elif (i,j==0,0):
#         return img
#
#     img[i, j] = 255
#     Case1(img, i + 1, j + 1)
#
#     else:
#         return img

#
#
# def contLines(mat,img):
#     print mat
#     flag=1
#     flag2=1
#     D = mat.shape
#     L=img.shape
#     if len(D) == 2 and len(L)==2:
#         m,n = D
#         newMat = np.zeros((m+2,n+2))
#         newMat[1:m+1, 1:n+1] = mat
#         newImg=np.zeros((m+2,n+2))
#         newImg[1:m+1,1:n+1]=img
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#
#                 if(newMat[i,j]==45):
#                     if flag:
#                         recContLines(newMat,newImg,i,j)
#                         flag=0
#
#                 # if(newMat[i,j]==-135):
#                 #     if flag2:
#                 #         recContLines(newMat, newImg, i, j)
#                 #         flag2=0
#                 #     if(img[i,j]==255):
#                 #         k=i
#                 #         r=j
#                 #         while(k!=0 and r!=n):
#                 #
#                 #             newImg[k,r]=0
#                 #             k-=1
#                 #             r+=1
#
#
#
#         return np.uint8(newImg)
#
#     elif len(D) == 3 and len(L)==3:
#
#         b, g, r = cv2.split(mat)
#         bb,gg,rr=cv2.split(img)
#         return cv2.merge((contLines(b, bb), contLines(g, gg), contLines(r, rr)))
#
#
#     else:
#         return None
