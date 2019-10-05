import scipy.misc
import glob
import indicoio
from indicoio.custom import Collection

# Configure API key for indico
indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'

# Connect to facial recognition collection
collection = Collection("facial_recognition three")

# Look for a face in the image given, localize it, save it, and predict whose face it belongs to
def testFaceImage(urlin, imgout):
    face = indicoio.facial_localization(urlin, sensitivity=0.05, crop=True)
    # print(face)
    if len(face) >= 1:
        face = face[0]
        face = face['image']

        scipy.misc.imsave(imgout, face)

        prediction = collection.predict(imgout)

        print(prediction)

        max = 0
        biggest = ""
        for key, value in prediction.items():
            if value > max:
                biggest = key
                max = value

        if max > 0.80:
            print("I'm sure this is " + biggest + " with "+ str(round(max * 100)) + "% accuracy\n")
        elif max > 0.60:
            print("I think this is " + biggest + " with "+ str(round(max * 100)) + "% accuracy\n")
        else:
            print("I'm guessing this is " + biggest + " with " + str(round(max * 100)) + "% accuracy\n")

    else:
        print("This one was too tricky :/ \n")


print("Starting facial recognition tests...\n")

# Loop through testing images
i = 1
for imgin in glob.iglob(r'C:\Users\Jason\Downloads\img_in\test\*.jpg'):
    # print(imgin)
    imgout = r"C:\Users\Jason\Downloads\img_out\test\test" + str(i) + ".jpg"
    print("Image Number " + str(i) + ":")
    testFaceImage(imgin, imgout)
    # print(imgout)
    i += 1

print("Facial recognition testing complete!")
