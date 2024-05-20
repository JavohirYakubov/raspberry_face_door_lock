from sklearn.metrics import classification_report, accuracy_score

def evaluate_model(recognizer, face_cascade, test_data_dir):
    y_true = []
    y_pred = []

    for file_name in os.listdir(test_data_dir):
        if file_name.startswith("User"):
            label = int(file_name.split('.')[1])
            image_path = os.path.join(test_data_dir, file_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces = face_cascade.detectMultiScale(image)

            for (x, y, w, h) in faces:
                roi = image[y:y + h, x:x + w]
                predicted_label, confidence = recognizer.predict(roi)
                y_true.append(label)
                y_pred.append(predicted_label)
    
    print("Classification Report:")
    print(classification_report(y_true, y_pred))
    print("Accuracy Score:")
    print(accuracy_score(y_true, y_pred))

# Load trained model and cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('/home/devapp/Documents/projects/raspberry_face_id/trainer.yml')

# Evaluate the model
evaluate_model(face_recognizer, face_cascade, "/home/devapp/Documents/projects/raspberry_face_id/test_dataset")
