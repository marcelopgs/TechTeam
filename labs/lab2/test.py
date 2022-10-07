import cv2


def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)


walter = cv2.imread('C:\\Users\\Waltinho\\minami\\TechTeam\\labs\\lab2\imagens\\11010031.jpg')
waltericone = cv2.imread('C:\\Users\\Waltinho\\minami\\TechTeam\\labs\\lab2\imagens\\waltericone.png')

joao = cv2.imread('C:\\Users\\Waltinho\\minami\\TechTeam\\labs\\lab2\imagens\\11010037.jpg')
adinan = cv2.imread('C:\\Users\\Waltinho\\minami\\TechTeam\\labs\\lab2\imagens\\11010043.jpg')

gray = cv2.cvtColor(walter, cv2.COLOR_BGR2GRAY)

width = int(walter.shape[1] * 25 / 100)
height = int(walter.shape[0] * 25 / 100)
dim = (width, height)
resized25 = cv2.resize(walter, dim, interpolation = cv2.INTER_AREA)


width2 = int(walter.shape[1] * 50 / 100)
height2 = int(walter.shape[0] * 50 / 100)
dim2 = (width2, height2)
resized50 = cv2.resize(walter, dim2, interpolation = cv2.INTER_AREA)

walterconcat = hconcat_resize_min([walter, waltericone],interpolation=cv2.INTER_CUBIC)
cv2.imshow('Original image',walter)
cv2.imshow('Gray image', gray)
cv2.imshow("25% image", resized25)
cv2.imwrite('walter25.jpg',resized25)
cv2.imshow("50% image", resized50)
cv2.imshow("walter icone", walterconcat)
cv2.imwrite('waltericone.jpg',walterconcat)

cv2.imwrite('walter50.jpg',resized50)
cv2.imwrite('waltergray.jpg',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

