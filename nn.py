import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from PIL import Image
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import glob
import os
import warnings
warnings.filterwarnings("ignore")



def right():
    keyboard.release(left)
    keyboard.press(right)


def left():
    keyboard.release(keyboard.KEY_RIGHT)
    keyboard.press(K_LEFT)



def move():
    randint (début, fin)


# A function for get images and their labels by given image paths
def get_data(images):
    X = []      # A list for store the images
    Y = []      # A list for store the labels

        X = [game.player.rect.x,
             game.player.rect.y,
             enemy_list = game.all_enemy.sprites()


    for i in range(3):
        Y = np.array([i,enemy_list[i].rect.x,enemy_list[i].rect.y,enemy_list[i].velocity])
        print(Y)

    X = np.array(X)                                         # Convert list X to numpy array
    X = X.reshape(X.shape[0], width, height, 1)             # Reshape the X

    return X, Y


# A function for convert labels to onehot labels for training
def onehot_labels(labels):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(labels)
    onehot_encoder = OneHotEncoder(sparse = False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded),1)
    onehot_labels = onehot_encoder.fit_transform(integer_encoded)
    return onehot_labels


# A function for create a CNN model and return it
def get_CNN_model():
    model = Sequential()

    model.add(Conv2D(16, kernel_size=(3,3), activation="relu", input_shape=(width, height, 1)))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(32, kernel_size=(3,3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(64, kernel_size=(3,3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.5)) # For regularization
    model.add(Dense(3, activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    return model


# Plot number of data categorical
def plot_data():
    # Plot number of the data for each class
    sns.countplot(Y)
    values, counts = np.unique(Y, return_counts=True)
    print(values, counts)
    plt.title('Number of data for each class')
    plt.show()

    # Plot number of the data for train and test set
    train_size = int(len(images)*0.9)  # %90
    test_size = int(len(images)*0.1)   # %10
    print('train: ' + str(train_size), ' - test: ' + str(test_size))
    sets = ['Train', 'Test']
    number_of_data = [train_size, test_size]
    plt.bar(sets, number_of_data, color=['orange', "teal"])
    plt.title('Number of data for train and test set')
    plt.ylabel('count')
    plt.show()


# Plot confusion matrix of trained model
def plot_confusion_matrix():
    y_pred = model.predict(test_X)
    y_pred = np.argmax(y_pred, axis=1)
    test_y_new = np.argmax(test_y, axis=1)

    cm = confusion_matrix(test_y_new, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["down", "right", "up"])

    disp = disp.plot(include_values=True, cmap='Blues', ax=None, xticks_rotation='horizontal')
    plt.title('Confusion Matrix')
    plt.show()


# Plot accuracy and loss of the model while training
def plot_accuracy_and_loss():
    plt.plot(history.history['accuracy'], linewidth=2)
    plt.title('Train Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.show()

    plt.plot(history.history['loss'], color='orange', linewidth=2)
    plt.title('Train Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.show()



# MAIN PROGRAM
if __name__ == "__main__":
    images = glob.glob("./dataset/*.png")    # Get all image paths with glob

    X, Y = get_images_and_labels(images)    # Get images and their labels

    plot_data() # Plot number of data categorical

    Y = onehot_labels(Y)                    # Convert labels to onehot labels ==> down: 100, right: 010, up: 001

    train_X, test_X, train_y, test_y = train_test_split(X, Y, test_size=0.1, random_state=10)  # Split the dataset
    model = get_CNN_model()
    print(model.summary()) # Print model summary

    history = model.fit(train_X, train_y, epochs=5, batch_size=64)

    train_accuracy = model.evaluate(train_X, train_y)
    print("Train accuracy: %", train_accuracy[1]*100)

    test_accuracy = model.evaluate(test_X, test_y)
    print("Test accuracy: %", test_accuracy[1]*100)

    plot_accuracy_and_loss()    # Plot accuracy and loss of the model while training
    plot_confusion_matrix()     # Plot confusion matrix of trained model

    open("model.json","w").write(model.to_json())
    model.save_weights("weights.h5")
