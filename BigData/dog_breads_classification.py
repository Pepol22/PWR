import tensorflow as tf
from tensorflow.keras.applications.resnet_v2 import ResNet152V2
from tensorflow.keras.applications import ResNet50V2
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import os
import matplotlib.pyplot as plt
import numpy as np
import json
import time

class DogBreedClassification:
    def __init__(self, path):
        self.path = path
        self.breeds = []
        self.resnet152_path = os.path.join(os.getcwd(), "resnet152")
        self.resnet50_path = os.path.join(os.getcwd(), "resnet50")
        self.validation_results = []

    def load_data(self, path):
        # Uzyskanie wszystkich ras psow
        for folder in os.listdir(path):
            breed = folder.split("-")[1]
            self.breeds.append(breed)
        print("Ilosc ras: ", len(self.breeds))
        print(self.breeds)

        # Ladowanie danych za pomoca keras.preprocessing oraz podzial na zbiory testowe i treningowe
        batch_size = 32  # ilosc obrazkow przetwarzana na raz
        validation_split = 0.2  # procent danych uzytych do testowania (wybrane 20%)

        self.train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            directory=path,
            label_mode='int',
            batch_size=batch_size,
            validation_split=validation_split,
            subset="training",
            seed=1024,
            shuffle=True
        )

        self.test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            directory=path,
            label_mode='int',
            batch_size=batch_size,
            validation_split=validation_split,
            subset="validation",
            seed=1024,
            shuffle=True
        )

        # Wizualizacja pierwszych 5 danych z pierwszego zbioru
        for image, label in self.train_dataset.take(1):
            for i in range(5):
                plt.imshow(image[i].numpy().astype('uint8'))
                plt.title(label[i].numpy().astype('uint8'))
                plt.show()

    # Zbior danych nie jest duzy, zatem dodajemy losowosc poprzez obracanie i odwracanie danych
    def augment_data(self):
        data_augmentation = tf.keras.Sequential([
            tf.keras.layers.RandomFlip('horizontal_and_vertical'),
            tf.keras.layers.RandomRotation(0.2),
        ])

        self.augmented_train_dataset = self.train_dataset.map(lambda x, y: (data_augmentation(x, training=True), y))

        # Wizualizacja pierwszych 5 danych po obracaniu
        for image, label in self.augmented_train_dataset.take(1):
            for i in range(5):
                plt.imshow(image[i].numpy().astype('uint8'))
                plt.title(label[i].numpy().astype('uint8'))
                plt.show()

    def resnet152_extract_features(self):
        # Inicjalizacja modelu ResNet152
        resnet = ResNet152V2(weights='imagenet', include_top=False, pooling='avg')
        normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1. / 255)
        self.resnet152_train_dataset = self.augmented_train_dataset.map(lambda x, y: (normalization_layer(x), y))

        # Ekstrakcja cech z danych treningowych
        train_features, train_labels = [], []

        for images, labels in self.resnet152_train_dataset:
            features = resnet.predict(images)
            train_features.extend(features)
            train_labels.extend(labels.numpy())

        self.test_dataset = self.test_dataset.map(lambda x, y: (normalization_layer(x), y))

        # Zapisanie wyekstraktowanych cech i etykiet do plikow
        train_features_file = os.path.join(self.resnet152_path, "resnet152_train_features.npy")
        train_labels_file = os.path.join(self.resnet152_path, "resnet152_train_labels.npy")
        np.save(train_features_file, np.array(train_features))
        np.save(train_labels_file, np.array(train_labels))
        # print(train_features)

        # Ekstrakcja cech z danych testowych
        test_features,test_labels = [], []


        for images, labels in self.test_dataset:
            features = resnet.predict(images)
            test_features.extend(features)
            test_labels.extend(labels.numpy())

        # Zapisanie wyekstraktowanych cech i etykiet do plikow
        test_features_file = os.path.join(self.resnet152_path, "resnet152_test_features.npy")
        test_labels_file = os.path.join(self.resnet152_path, "resnet152_test_labels.npy")
        np.save(test_features_file, np.array(test_features))
        np.save(test_labels_file, np.array(test_labels))

    def resnet152_features_classification(self):
        # Odczytywanie cech oraz etykiet danych z odpowiednich plikow
        train_features = np.load(os.path.join(self.resnet152_path, "resnet152_train_features.npy"))
        train_labels = np.load(os.path.join(self.resnet152_path, "resnet152_train_labels.npy"))
        test_features = np.load(os.path.join(self.resnet152_path, "resnet152_test_features.npy"))
        test_labels = np.load(os.path.join(self.resnet152_path, "resnet152_test_labels.npy"))

        self.k_nearest_neighbours("Resnet152", test_features, train_features, test_labels, train_labels)
        self.SVM_classification("Resnet152", test_features, train_features, test_labels, train_labels)
        self.RandomForest_classification("Resnet152", test_features, train_features, test_labels, train_labels)

    def resnet50_extract_features(self):
        # Inicjalizacja modelu ResNet50
        resnet = ResNet50V2(weights='imagenet', include_top=False, pooling='avg')
        # Przeskalowanie danych
        normalization_layer = Rescaling(1. / 255)
        self.resnet50_train_dataset = self.augmented_train_dataset.map(lambda x, y: (normalization_layer(x), y))

        # Ekstrakcja cech z danych treningowych
        train_features, train_labels = [], []

        for images, labels in self.resnet50_train_dataset:
            features = resnet.predict(images)
            train_features.extend(features)
            train_labels.extend(labels.numpy())

        # Zapisanie wyekstraktowanych cech i etykiet do plików
        train_features_file = os.path.join(self.resnet50_path, "resnet50_train_features.npy")
        train_labels_file = os.path.join(self.resnet50_path, "resnet50_train_labels.npy")
        np.save(train_features_file, np.array(train_features))
        np.save(train_labels_file, np.array(train_labels))

        # Ekstrakcja cech z danych testowych
        test_features, test_labels = [], []

        # Przeskalowanie danych
        self.test_dataset = self.test_dataset.map(lambda x, y: (normalization_layer(x), y))

        for images, labels in self.test_dataset:
            features = resnet.predict(images)
            test_features.extend(features)
            test_labels.extend(labels.numpy())

        # Zapisanie wyekstraktowanych cech i etykiet do plików
        test_features_file = os.path.join(self.resnet50_path, "resnet50_test_features.npy")
        test_labels_file = os.path.join(self.resnet50_path, "resnet50_test_labels.npy")
        np.save(test_features_file, np.array(test_features))
        np.save(test_labels_file, np.array(test_labels))

    def resnet50_features_classification(self):
        # Odczytywanie cech oraz etykiet danych z odpowiednich plikow
        train_features = np.load(os.path.join(self.resnet50_path, "resnet50_train_features.npy"))
        train_labels = np.load(os.path.join(self.resnet50_path, "resnet50_train_labels.npy"))
        test_features = np.load(os.path.join(self.resnet50_path, "resnet50_test_features.npy"))
        test_labels = np.load(os.path.join(self.resnet50_path, "resnet50_test_labels.npy"))

        self.k_nearest_neighbours("Resnet50", test_features, train_features, test_labels, train_labels)
        self.SVM_classification("Resnet50", test_features, train_features, test_labels, train_labels)
        self.RandomForest_classification("Resnet50", test_features, train_features, test_labels, train_labels)

    # K najblizszych sasiadow
    def k_nearest_neighbours(self, extraction_method, test_features, train_features, test_labels, train_labels):
        start_time = time.time()
        k = 18 # Liczba sasiadow
        KNN = KNeighborsClassifier(n_neighbors=k)
        KNN.fit(train_features, train_labels)

        # Predykcja etykiet klas
        predicted_labels = KNN.predict(test_features)

        # Ocena jakosci klasyfikatora
        end_time = time.time()
        execution_time = end_time-start_time
        self.validate_classifier(test_labels, predicted_labels, "K Nearest Neighbours", extraction_method, execution_time)

    # Maszyna wektorow nosnych
    def SVM_classification(self, extraction_method, test_features, train_features, test_labels, train_labels):
        start_time = time.time()
        # Inicjalizacja oraz trenowanie klasyfikatora
        SVM_classificator = SVC()
        SVM_classificator.fit(train_features, train_labels)

        # Predykcja etykiet klas
        predicted_labels = SVM_classificator.predict(test_features)

        end_time = time.time()
        execution_time = end_time - start_time
        # Ocena jakosci klasyfikatora
        self.validate_classifier(test_labels, predicted_labels, "Support Vector Machines Classifier", extraction_method, execution_time)

    # Las losowych drzew decyzyjnych
    def RandomForest_classification(self, extraction_method, test_features, train_features, test_labels, train_labels):
        start_time = time.time()
        # Inicjalizacja oraz trenowanie klasyfikatora
        RFC = RandomForestClassifier(n_estimators=1000)
        RFC.fit(train_features, train_labels)

        # Predykcja etykiet klas
        predicted_labels = RFC.predict(test_features)

        end_time = time.time()
        execution_time = end_time - start_time
        # Ocena jakosci klasyfikatora
        self.validate_classifier(test_labels, predicted_labels, "Random Forest Classifier", extraction_method, execution_time)

    def validate_classifier(self, test_labels, predicted_labels, name, extraction_method, time):
        # Ocena jakosci klasyfikatora
        f1 = f1_score(test_labels, predicted_labels, average='weighted')
        accuracy = accuracy_score(test_labels, predicted_labels)
        print(f"Metoda ekstrakcji: {extraction_method}, Nazwa klasyfikatora: {name} Czas: {time}\nMiara dokladnosci: {accuracy}, miara f-1: {f1}")

        result = "Metoda ekstrakcji: " + extraction_method + "\n Nazwa klasyfikatora: " + name + "Czas: " + str(time) + ", Miara dokladnosci: " + str(accuracy) +  ", miara f-1: " + str(f1)
        self.validation_results.append(result)

    def save_validation_results(self):
        # Zapisywanie miar oceny jakosci klasyfikatora do pliku
        with open("Classifier_Validation_results.json", "a") as file:
            json.dump(self.validation_results, file)

path = os.path.join(os.curdir + "/dogs_data/")
classificator = DogBreedClassification(path)
classificator.load_data(path)
classificator.augment_data()

classificator.resnet152_extract_features()
classificator.resnet152_features_classification()

classificator.resnet50_extract_features()
classificator.resnet50_features_classification()

classificator.save_validation_results()
