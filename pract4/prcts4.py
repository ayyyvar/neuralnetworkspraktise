from keras.preprocessing import image
from keras.models import Model
import numpy as np

img_path = 'pictures/1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

# Xception
from keras.applications.xception import Xception, preprocess_input, decode_predictions
x = preprocess_input(x)
model = Xception(weights='imagenet')
preds_mobile = model.predict(x)
print('Xception Predicted:', decode_predictions(preds_mobile, top=5)[0])

# VGG19
from keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions
x = preprocess_input(x)
model = VGG19(weights='imagenet')
preds_mobile = model.predict(x)
print('VGG16 Predicted:', decode_predictions(preds_mobile, top=5)[0])

# ResNet50
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
x = preprocess_input(x)
model = ResNet50(weights='imagenet')
preds_resnet50 = model.predict(x)
print('ResNet50 Predicted:', decode_predictions(preds_resnet50, top=5)[0])


# DenseNet121
from keras.applications.densenet import DenseNet121, preprocess_input, decode_predictions
x = preprocess_input(x)
model = DenseNet121(weights='imagenet')
preds_mobile = model.predict(x)
print('DenseNet121 Predicted:', decode_predictions(preds_mobile, top=5)[0])


# InceptionResNetV2
from keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input, decode_predictions
x = preprocess_input(x)
model = InceptionResNetV2(weights='imagenet')
preds_mobile = model.predict(x)
print('InceptionResNetV2 Predicted:', decode_predictions(preds_mobile, top=5)[0])