import cv2
import numpy as np
import face_recognition

imgtegan = face_recognition.load_image_file('imageattendance/tegan.jpg')
imgtegan = cv2.cvtColor(imgtegan,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('tegan2.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceloc =face_recognition.face_locations(imgtegan)[0]
encodetegan = face_recognition.face_encodings(imgtegan)[0]
cv2.rectangle(imgtegan,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

facelocTest =face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(255,0,255),2)

result = face_recognition.compare_faces([encodetegan],encodeTest)
faceDis = face_recognition.face_distance([encodetegan],encodeTest  )
print(result,faceDis)
cv2.putText(imgTest,f'{result} {round(faceDis[0]),2}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)



cv2.imshow('tegan',imgtegan)
cv2.imshow('tegan2',imgTest)
cv2.waitKey(0)
