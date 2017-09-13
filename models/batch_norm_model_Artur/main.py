import sys
sys.path.insert(0, "/input/") #for cloud
sys.path.insert(0, "../common/") #for local
import common

from keras.models import Sequential
from keras.layers import *

model = Sequential()
model.add(Conv2D(8, (3, 3), padding='same',
          input_shape=(common.resolution_x, common.resolution_y, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(16, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.15))
model.add(Conv2D(8, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(24, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Conv2D(12, (3, 3), padding='same'))
model.add(Dropout(0.25))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(Conv2D(16, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(BatchNormalization())
model.add(GlobalAveragePooling2D())
for i in range(1):
    model.add(Dense(16))
    model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

common.experiment(model)
