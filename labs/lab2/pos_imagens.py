import cv2

# Import das imagens
walter = cv2.imread('C:\\Users\\Waltinho\\minami\\TechTeam\\labs\\lab2\imagens_editadas\\walter_100.jpg')
joao = cv2.imread('C:\\Users\\Waltinho\\minami\\TechTeam\\labs\\lab2\imagens_editadas\\joao_100.jpg')
grupo = cv2.imread('C:\\Users\\Waltinho\\minami\\TechTeam\\labs\\lab2\imagens_editadas\\foto_grupo.jpg')

# Conversão
walter_gray = cv2.cvtColor(walter, cv2.COLOR_BGR2GRAY)
joao_gray = cv2.cvtColor(joao, cv2.COLOR_BGR2GRAY)
grupo_gray = cv2.cvtColor(grupo, cv2.COLOR_BGR2GRAY)

cv2.imwrite('walter_cinza.jpg',walter_gray)
cv2.imwrite('joao_cinza.jpg',joao_gray)
cv2.imwrite('grupo_cinza.jpg',grupo_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

