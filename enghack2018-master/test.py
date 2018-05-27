import scipy.misc
import indicoio
import numpy as np

indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'


def saveFaceImage(urlin, urlout):
    face = indicoio.facial_localization(urlin,
                                    sensitivity=0, crop=True)
    face = face[0]
    face = face['image']

    scipy.misc.imsave(urlout, face)

urlin = r"https://peopledotcom.files.wordpress.com/2018/04/will-ferrell.jpg"
urlout = r"C:\Users\ldann\Downloads\outfile1.jpg"
saveFaceImage(urlin, urlout)
saveFaceImage(r"C:\Users\ldann\Downloads\img_in\jeffrey.jpg", r"C:\Users\ldann\Downloads\outfile2.jpg")