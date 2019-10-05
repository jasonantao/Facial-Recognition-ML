import indicoio

from indicoio.custom import Collection

indicoio.config.api_key = '3244a46ccac6ac4cf7d163a6240b5531'

collection = Collection("facial_recognition three")

collection.train()
collection.wait()

print("Training complete!")
