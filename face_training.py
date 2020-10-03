import cv2
import numpy as np
from PIL import Image
import os

def Start():
    # Path for face image database
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # function to get the images and label data
    detector = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        imagePaths.remove("dataset/data.JSON")
        for each in imagePaths:
            if each == "dataset/data.JSON":
                print("Error : Could not remove data.JSON")
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            if imagePath == "dataset/data.JSON":
                continue
            PIL_img = Image.open(imagePath).convert('L')  # grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)
        return faceSamples, ids
    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, ids = getImagesAndLabels(path)
    # Save the model into trainer/trainer.yml
    recognizer.train(faces, np.array(ids))
    # Print the numer of faces trained and end program
    recognizer.write('trainer/trainer.yml')
    print("\n [INFO] {0} faces trained. Exiting Program".format(
        len(np.unique(ids))))
Start()
