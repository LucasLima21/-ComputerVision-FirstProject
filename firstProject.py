"""
UEA - Universidade do Estado do Amazonas
EST - Escola Superior de Tecnologia
Primeira Atividade Visão Computacional(Computer Vision)
Grupo : Karla Félix, Lucas Lima, Victor Lopes 
E-mail: ldsllm.eng@uea.edu.br
"""

import cv2
import numpy as np
black = (0,0,0)

def copyImage(image):
    return np.copy(image)

def groupNameComponents(image):
    font = cv2.FONT_HERSHEY_SIMPLEX
    return cv2.putText(copyImage(image), 'Karla Felix, Lucas Lima e Victor Lopes', (3, 50), font, 1, black, 1, cv2.LINE_AA)

def circle(image):
    height, weight = copyImage(image).shape[:2]
    return cv2.circle(copyImage(image), (height-200, weight-400), 100, black, -1)

def flip(image):
    return cv2.flip(copyImage(image), 0)

def crop(image):
    return copyImage(image)[200:800, 100:600]

def results(image):
    
    imageGroupName = groupNameComponents(image)
    imageCircle = circle(image)
    imageFlip = flip(image)
    imageCropped = crop(image)
    return [image, imageGroupName, imageCircle, imageFlip, imageCropped]
    
        

def showResults():
    image = cv2.imread('manaus.jpg', 1)
    result = results(image)
    imageStrings = ['Original', 'Integrantes do Grupo', 'Círculo', 'Giro Horizontal', 'Image Cortada']
    for i in range(len(result)):
        cv2.imshow(imageStrings[i], result[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

showResults()

