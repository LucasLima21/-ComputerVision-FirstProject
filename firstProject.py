"""
UEA - Universidade do Estado do Amazonas
EST - Escola Superior de Tecnologia
Primeira Atividade Visão Computacional(Computer Vision)
Grupo : Karla Félix, Lucas Lima, Victor Lopes 
E-mail: ldsllm.eng@uea.edu.br
"""

import cv2
import numpy as np
blue = (255,0,0)

def getHeightAndWidth(image):
    height, width = image.shape[:2]
    return height, width

def copyImage(image):
    return np.copy(image)

def groupNameComponents(image):
    font = cv2.FONT_HERSHEY_SIMPLEX
    saveImage = copyImage(image)
    height, width = getHeightAndWidth(saveImage)
    return cv2.putText(saveImage, 'Karla Felix, Lucas Lima e Victor Lopes', (height - 500, width - 260), font, 1, blue, 1 , cv2.LINE_AA)

def circle(image):
    saveImage = copyImage(image)
    height, width = getHeightAndWidth(saveImage)
    return cv2.circle(saveImage, (height-200, width-400), 100, blue, -1)

def flip(image):
    return cv2.flip(copyImage(image), 0)

def crop(image):
    height, width = getHeightAndWidth(image)
    return image[200:800, 200:600]

def results(image):
    imageGroupName = groupNameComponents(image)
    imageCircle = circle(image)
    imageFlip = flip(image)
    imageCropped = crop(image)
    return [image, imageGroupName, imageCircle, imageFlip, imageCropped]
    
        
def showResults():
    image = cv2.imread('chernobilly.jpeg', 1)
    print(image.shape[0], image.shape[1])
    result = results(image)
    imageStrings = ['Original', 'Integrantes do Grupo', 'Circulo', 'Giro Horizontal', 'Image Cortada']
    for i in range(len(result)):
        cv2.imshow(imageStrings[i], result[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

showResults()

