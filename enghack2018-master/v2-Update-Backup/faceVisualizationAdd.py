import scipy.misc
import glob

import indicoio

from indicoio.custom import Collection

indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'

collection = Collection("facial_recognition three")


def saveFaceImage(urlin, urlout, name):
    face = indicoio.facial_localization(urlin, sensitivity=0.3, crop=True)
    print(face)
    if len(face) >= 1:
        face = face[0]
        face = face['image']

        scipy.misc.imsave(urlout, face)

        collection.add_data([urlout, name])


i = 0
for imgin in glob.iglob(r'C:\Users\ldann\Downloads\img_in\jason\*.jpg'):
    print(imgin)
    imgout = r"C:\Users\ldann\Downloads\img_out\jason\img" + str(i) + ".jpg"
    saveFaceImage(imgin, imgout, "Jason")
    print(imgout)
    i += 1

i = 0
for imgin in glob.iglob(r'C:\Users\ldann\Downloads\img_in\jeffrey\*.jpg'):
    print(imgin)
    imgout = r"C:\Users\ldann\Downloads\img_out\jeffrey\img" + str(i) + ".jpg"
    saveFaceImage(imgin, imgout, "Jeffrey")
    print(imgout)
    i += 1

i = 0
for imgin in glob.iglob(r'C:\Users\ldann\Downloads\img_in\danny\*.jpg'):
    print(imgin)
    imgout = r"C:\Users\ldann\Downloads\img_out\danny\img" + str(i) + ".jpg"
    saveFaceImage(imgin, imgout, "Danny")
    print(imgout)
    i += 1

collection.train()
collection.wait()

print("Adding complete!")
