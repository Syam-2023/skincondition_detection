# # from flask import Flask, render_template, request
# # import tensorflow as tf
# # from tensorflow import keras
# # from keras.models import load_model
# # from keras.preprocessing import image
# # import numpy as np
# # import os


# # app = Flask(__name__)


# # # Load the trained model
# # model_path = 'models/my_model.h5'  # Adjust the path if necessary
# # if os.path.exists(model_path):
# #     model = load_model(model_path)
# # else:
# #     raise FileNotFoundError(f"Model file not found at {model_path}")


# # # Define a function to preprocess the image
# # def preprocess_image(img_path):
# #     img = image.load_img(img_path, target_size=(150, 150))
# #     img_array = image.img_to_array(img)
# #     img_array = np.expand_dims(img_array, axis=0)
# #     img_array /= 255.0
# #     return img_array

# # @app.route('/')
# # def home():
# #     return render_template('index.html')


# # @app.route('/predict',methods=['POST'])
# # def predict():
# #     if 'file' not in request.files:
# #         return redirect(request.url)
    
# #     file = request.files['file']
# #     if file.filename == '':
# #         return redirect(request.url)
    
# #     if file:
# #         file_path = os.path.join('uploads', file.filename)
# #         file.save(file_path)
        
# #         # Preprocess the image
# #         img_array = preprocess_image(file_path)
        
# #         # Make a prediction
# #         prediction = model.predict(img_array)
# #         predicted_class = np.argmax(prediction, axis=1)[0]
        
# #         # Map predicted class index to class name (adjust based on your class indices)
# #         class_indices = {0: 'Class 0', 1: 'Class 1', 2: 'Class 2'}  # Replace with your actual class names
# #         result = class_indices[predicted_class]
        
# #         return render_template('index.html', prediction=result)

# # if __name__ == "__main__":
# #     if not os.path.exists('uploads'):
# #         os.makedirs('uploads')
# #     app.run(host='0.0.0.0', port=8080, debug=True)

# from flask import Flask, render_template, request, redirect
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import os

# from ultralytics import YOLO
# import cv2

# app = Flask(__name__)

# # Load the trained model
# model_path = 'models/my_model.h5'  # Ensure this path is correct
# try:
#     model = load_model(model_path)
#     model.save('models/my_model_updated.h5')
# except Exception as e:
#     raise FileNotFoundError(f"Failed to load model at {model_path}. Error: {str(e)}")

# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return redirect(request.url)
    
#     file = request.files['file']
#     if file.filename == '':
#         return redirect(request.url)
    
#     if file:
#         file_path = os.path.join('uploads', file.filename)
#         file.save(file_path)
        
#         img_array = preprocess_image(file_path)

#         # Load the YOLO model
#         model_yolo = YOLO('yolov8m.pt')  # Load the pre-trained YOLOv8 nano model
#         url_image = cv2.imread(file_path)
#         result_yolo = model_yolo(url_image)

#         for result in result_yolo:
#             for box in result.boxes:
#                 if int(box.cls[0]) == 0:
#                     print("human")
#                 else:
#                     print("object")
        
#         prediction = model.predict(img_array)
#         predicted_class = np.argmax(prediction, axis=1)[0]
        
#         class_indices = {0: 'Acne', 1: 'Clear', 2: 'Comedone'}
#         result = class_indices.get(predicted_class, 'Unknown condition')
        
#         return render_template('index.html', prediction=result)

# if __name__ == "__main__":
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(host='0.0.0.0', port=8080, debug=True)
# from flask import Flask, render_template, request, jsonify
# import tensorflow as tf
# from tensorflow import keras
# from keras.models import load_model
# from keras.preprocessing import image
# import numpy as np
# import os
# import base64
# from PIL import Image
# import io

# app = Flask(__name__)

# # Load the trained model
# model_path = 'models/my_model.h5'  # Adjust the path if necessary
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     raise FileNotFoundError(f"Model file not found at {model_path}")

# # Define a function to preprocess the image
# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# # Define a function to preprocess the image from base64 data
# def preprocess_image_from_base64(base64_str):
#     img = Image.open(io.BytesIO(base64.b64decode(base64_str)))
#     img = img.resize((150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' in request.files and request.files['file'].filename != '':
#         file = request.files['file']
#         file_path = os.path.join('uploads', file.filename)
#         file.save(file_path)
        
#         # Preprocess the image
#         img_array = preprocess_image(file_path)
#     elif 'image_data' in request.form:
#         base64_image = request.form['image_data']
#         img_array = preprocess_image_from_base64(base64_image)
#     else:
#         return jsonify({'error': 'No image provided'}), 400
    
#     # Make a prediction
#     prediction = model.predict(img_array)
#     predicted_class = np.argmax(prediction, axis=1)[0]
    
#     # Map predicted class index to class name (adjust based on your class indices)
#     class_indices = {0: 'Acne', 1: 'Clear Skin', 2: 'Comedone'}  # Replace with your actual class names
#     result = class_indices.get(predicted_class, 'Unknown Condition')
    
#     return jsonify({'prediction': result})

# if __name__ == "__main__":
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(host='0.0.0.0', port=8080, debug=True)

# using this again
# from flask import Flask, render_template, request, jsonify
# import tensorflow as tf
# from tensorflow import keras
# from keras.models import load_model
# from keras.preprocessing import image
# import numpy as np
# import os
# import base64
# from PIL import Image
# import io

# app = Flask(__name__)

# # Load the trained model
# model_path = 'models/my_model.h5'  # Adjust the path if necessary
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     raise FileNotFoundError(f"Model file not found at {model_path}")

# # Define a function to preprocess the image
# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# # Define a function to preprocess the image from base64 data
# def preprocess_image_from_base64(base64_str):
#     img = Image.open(io.BytesIO(base64.b64decode(base64_str)))
#     img = img.resize((150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' in request.files and request.files['file'].filename != '':
#         file = request.files['file']
#         file_path = os.path.join('uploads', file.filename)
#         file.save(file_path)
        
#         # Preprocess the image
#         img_array = preprocess_image(file_path)
#     elif 'image_data' in request.form:
#         base64_image = request.form['image_data']
#         img_array = preprocess_image_from_base64(base64_image)
#     else:
#         return jsonify({'error': 'No image provided'}), 400
    
#     # Make a prediction
#     prediction = model.predict(img_array)
#     predicted_class = np.argmax(prediction, axis=1)[0]
    
#     # Map predicted class index to class name (adjust based on your class indices)
#     class_indices = {0: 'Acne', 1: 'Clear Skin', 2: 'Comedone'}  # Replace with your actual class names
#     result = class_indices.get(predicted_class, 'Unknown Condition')
    
#     return jsonify({'prediction': result})

# if __name__ == "__main__":
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(host='0.0.0.0', port=8080, debug=True)




# example 

# from flask import Flask, render_template, request, jsonify
# import tensorflow as tf
# from tensorflow import keras
# from keras.models import load_model
# from keras.preprocessing import image
# from sklearn.metrics.pairwise import cosine_similarity
# import pickle
# import numpy as np
# import os
# import base64
# from PIL import Image
# import io

# app = Flask(__name__)

# # Define the function to recommend products
# def recommend_products(normalized_user_profile, normalized_features, product_names, top_n=3):
#     # Compute cosine similarity between user profile and all products
#     user_sim = cosine_similarity(normalized_user_profile, normalized_features)

#     # Get the top N most similar products
#     top_indices = user_sim[0].argsort()[-(top_n+1):][::-1][1:]  # Skip the first one as it will be the user profile itself

#     # Get the product names of the top N recommendations
#     recommended_products = product_names.iloc[top_indices]

#     return recommended_products

# # Load the components
# def load_components():
#     with open('components(1).pkl', 'rb') as file:
#         return pickle.load(file)

# dataf, scaler, feature_columns, product_names = load_components()

# # Load the trained model
# model_path = 'models/my_model.h5'  # Adjust the path if necessary
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     raise FileNotFoundError(f"Model file not found at {model_path}")

# # Define a function to preprocess the image
# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# # Define a function to preprocess the image from base64 data
# def preprocess_image_from_base64(base64_str):
#     img = Image.open(io.BytesIO(base64.b64decode(base64_str)))
#     img = img.resize((150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' in request.files and request.files['file'].filename != '':
#         file = request.files['file']
#         file_path = os.path.join('uploads', file.filename)
#         file.save(file_path)
        
#         # Preprocess the image
#         img_array = preprocess_image(file_path)
#     elif 'image_data' in request.form:
#         base64_image = request.form['image_data']
#         img_array = preprocess_image_from_base64(base64_image)
#     else:
#         return jsonify({'error': 'No image provided'}), 400
    
#     # Make a prediction
#     prediction = model.predict(img_array)
#     predicted_class = np.argmax(prediction, axis=1)[0]
    
#     # Map predicted class index to class name (adjust based on your class indices)
#     class_indices = {0: 'Acne', 1: 'Clear Skin', 2: 'Comedone'}  # Replace with your actual class names
#     result = class_indices.get(predicted_class, 'Unknown Condition')
    
#     # Get user profile information
#     skin_type = request.form.get('skin_type')
#     concerns = request.form.getlist('concerns')
    
#     # Prepare user profile for recommendation
#     user_profile = {
#         'Combination': 1 if skin_type == 'combination' else 0,
#         'Dry': 1 if skin_type == 'dry' else 0,
#         'Oily': 1 if skin_type == 'oily' else 0,
#         'Sensitive': 1 if skin_type == 'sensitive' else 0,
#         'Acne': 1 if 'acne' in concerns else 0,
#         'Irritation': 1 if 'irritation' in concerns else 0,
#         'Broken barrier': 1 if 'broken-barrier' in concerns else 0,
#         'Dark Spots': 1 if 'dark-spots' in concerns else 0,
#         'Exfoliation': 1 if 'exfoliation' in concerns else 0,
#         'Hydration': 1 if 'hydration' in concerns else 0,
#         'Pigmentation': 1 if 'pigmentation' in concerns else 0,
#         'Pimples': 1 if 'pimples' in concerns else 0,
#         'Pores': 1 if 'pores' in concerns else 0,
#         'Skin soothing': 1 if 'skin-soothing' in concerns else 0,
#         'Sun protection': 1 if 'sun-protection' in concerns else 0,
#         'Whitehead/Blackhead': 1 if 'whitehead-blackhead' in concerns else 0
#     }
    
#     return jsonify({'prediction': result, 'user_profile': user_profile})

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     user_profile = request.json['user_profile']
#     normalized_user_profile = scaler.transform([list(user_profile.values())])
    
#     # Normalize the feature data
#     features = dataf[feature_columns]
#     normalized_features = scaler.transform(features)
    
#     recommended_products_list = recommend_products(normalized_user_profile, normalized_features, product_names)
    
#     return jsonify(recommended_products_list.tolist())

# if __name__ == "__main__":
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(host='0.0.0.0', port=8080, debug=True)


# import os
# import numpy as np
# import pandas as pd
# from flask import Flask, request, jsonify, render_template
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.preprocessing import LabelEncoder
# import pickle

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'

# # Load your models and encoders

# skin_condition_model = load_model('models/my_model_updated.h5')
# product_recommendation_model = pickle.load(open('components(1).pkl', 'rb'))
# label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

# product_data = pd.read_csv('Skinpro - Skinpro (2).csv.csv')

# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(224, 224))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# def recommend_products(user_profile):
#     # Calculate cosine similarity between user profile and product data
#     product_profiles = product_data.drop(['Product', 'product_url', 'product_pic'], axis=1)
#     similarities = cosine_similarity([user_profile], product_profiles)[0]
#     top_indices = similarities.argsort()[-5:][::-1]
#     return product_data.iloc[top_indices]

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     name = request.form['name']
#     age = int(request.form['age'])
#     skin_type = request.form['skin-type']
#     concerns = request.form.getlist('concerns')
    
#     # Create user profile
#     user_profile = np.zeros(len(product_data.columns) - 3)
#     for concern in concerns:
#         index = list(product_data.columns).index(concern)
#         user_profile[index - 3] = 1
    
#     # Save uploaded file
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
    
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
    
#     if file:
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)
        
#         # Preprocess the image
#         img_array = preprocess_image(file_path)
        
#         # Predict skin condition
#         predictions = skin_condition_model.predict(img_array)
#         predicted_class = label_encoder.inverse_transform([np.argmax(predictions)])
#         condition = predicted_class[0]
        
#         # Recommend products
#         recommendations = recommend_products(user_profile)
#         recommendations = recommendations.to_dict(orient='records')
        
#         return jsonify({'condition': condition, 'recommendations': recommendations})

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# import tensorflow as tf
# from tensorflow import keras
# from keras.models import load_model
# from keras.preprocessing import image
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.preprocessing import StandardScaler
# import numpy as np
# import pandas as pd
# import os
# import base64
# from PIL import Image
# import io

# app = Flask(__name__)

# # Load the trained model
# model_path = 'models/my_model.h5'  # Adjust the path if necessary
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     raise FileNotFoundError(f"Model file not found at {model_path}")


# # reading the data from dataset
# dataf = pd.read_csv('preprocessed_dataset_products.csv')

# # Define the unique feature columns
# feature_columns = [
#     'Combination', 'Dry', 'Oily', 'Sensitive', 'Acne', 'Irritation',
#     'Broken barrier', 'Dark Spots', 'Exfoliation', 'Hydration',
#     'Pigmentation', 'Pimples', 'Pores', 'Skin soothing', 'Sun protection',
#     'Whitehead/Blackhead'
# ]
# # Strip leading and trailing spaces from column names
# dataf.columns = dataf.columns.str.strip()
# # Ensure 'Product' column is string type
# dataf['Product'] = dataf['Product'].astype(str)
# # Define features and product names
# features = dataf[feature_columns]
# product_names = dataf['Product']

# # Normalize the feature data
# scaler = StandardScaler()
# normalized_features = scaler.fit_transform(features)
# # Get the product names
# product_names = dataf['Product']

# def get_user_profile(form_data):
#     # Extract user input from form data
#     user_input = {column: int(form_data.get(column, 0)) for column in feature_columns}

#     # Create a DataFrame from the user input
#     user_profile = pd.DataFrame([user_input], columns=features.columns)

#     # Normalize the user profile using the same scaler
#     normalized_user_profile = scaler.transform(user_profile)

#     return normalized_user_profile




# # Define a function to preprocess the image
# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# # Define a function to preprocess the image from base64 data
# def preprocess_image_from_base64(base64_str):
#     img = Image.open(io.BytesIO(base64.b64decode(base64_str)))
#     img = img.resize((150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' in request.files and request.files['file'].filename != '':
#         file = request.files['file']
#         file_path = os.path.join('uploads', file.filename)
#         file.save(file_path)
        
#         # Preprocess the image
#         img_array = preprocess_image(file_path)
#     elif 'image_data' in request.form:
#         base64_image = request.form['image_data']
#         img_array = preprocess_image_from_base64(base64_image)
#     else:
#         return jsonify({'error': 'No image provided'}), 400
    
#     # Make a prediction
#     prediction = model.predict(img_array)
#     predicted_class = np.argmax(prediction, axis=1)[0]
    
#     # Map predicted class index to class name (adjust based on your class indices)
#     class_indices = {0: 'Acne', 1: 'Clear Skin', 2: 'Comedone'}  # Replace with your actual class names
#     result = class_indices.get(predicted_class, 'Unknown Condition')
    
#     return jsonify({'prediction': result})

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     form_data = request.form
#     user_profile = get_user_profile(form_data)
#     recommended_products = recommend_products(user_profile, normalized_features, product_names, top_n=3)
    
#     return jsonify({'recommendations': recommended_products.tolist()})
# def recommend_products(normalized_user_profile, normalized_features, product_names, top_n=3):
#     # Compute cosine similarity between user profile and all products
#     user_sim = cosine_similarity(normalized_user_profile, normalized_features)

#     # Get the top N most similar products
#     top_indices = user_sim[0].argsort()[-(top_n+1):][::-1][1:]  # Skip the first one as it will be the user profile itself

#     # Get the product names of the top N recommendations
#     recommended_products = product_names.iloc[top_indices]

#     return recommended_products


# if __name__ == "main":
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(host='0.0.0.0', port=8080, debug=True)


# from flask import Flask, render_template, request, jsonify, session
# import tensorflow as tf
# from keras.models import load_model
# from keras.preprocessing import image
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.preprocessing import StandardScaler
# import numpy as np
# import pandas as pd
# import os
# import base64
# from PIL import Image
# import io
# import logging

# app = Flask(__name__)
# app.secret_key = b'\x93\x1f\xd7\xae\x92\xb2\xdd\xf7\xcbk\xc1e\xbf\x12\xd5M\xd3\x17v\xd9\x8fUj\xf7'  # Replace with your generated key

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)

# # Load the trained skin condition model
# model_path = 'models/my_model.h5'  # Adjust the path if necessary
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     raise FileNotFoundError(f"Model file not found at {model_path}")


# # reading the data from dataset
# dataf = pd.read_csv('preprocessed_dataset_products.csv')
# # Function to preprocess image
# def preprocess_image(img):
#     img = img.resize((224, 224))  # Resize image to the input size expected by the model
#     img = image.img_to_array(img) / 255.0  # Convert to array and normalize
#     img = np.expand_dims(img, axis=0)  # Add batch dimension
#     return img

# # Route for home page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route for predicting skin condition
# @app.route('/predict', methods=['POST'])
# def predict():
#     logging.debug("Received request for prediction")
#     data = request.get_json()
#     logging.debug(f"Data received: {data}")
#     image_data = base64.b64decode(data['image_data'])
#     img = Image.open(io.BytesIO(image_data))

#     processed_img = preprocess_image(img)
#     prediction = model.predict(processed_img)
#     predicted_class = np.argmax(prediction, axis=1)[0]

#     conditions = ['Acne', 'Pimple', 'Spots', 'Mole1', 'Mole2', 'Scar']
#     predicted_condition = conditions[predicted_class]

#     logging.debug(f"Prediction result: {predicted_condition}")
#     return jsonify({'prediction': predicted_condition})

# # Route for recommending products
# @app.route('/recommend', methods=['POST'])
# def recommend():
#     logging.debug("Received request for recommendation")
#     form_data = request.form.to_dict()
#     logging.debug(f"Form data received: {form_data}")
#     # Extract and clean input features
#     input_features = []
#     for key in form_data.keys():
#             try:
#                 value = form_data[key].strip()  # Remove any leading/trailing whitespace
#                 if value:
#                     input_features.append(float(value))
#                 else:
#                     input_features.append(0.0)  # Use a default value for missing or empty fields
#             except ValueError:
#                 logging.warning(f"Invalid value for {key}: {form_data[key]}")
#                 input_features.append(0.0)  # Use a default value for invalid entries


#     # Normalize input features
#     scaler = StandardScaler()
#     product_features = dataf.drop(columns=['Product', 'product_url', 'product_pic'])
#     scaled_features = scaler.fit_transform(product_features)
#     input_scaled = scaler.transform([input_features])

#     # Compute cosine similarities
#     similarities = cosine_similarity(input_scaled, scaled_features)
#     top_indices = similarities.argsort()[0][-3:][::-1]  # Get top 3 similar products

#     recommended_products = dataf.iloc[top_indices]

#     recommendations = recommended_products[['Product', 'product_url']].to_dict(orient='records')
#     logging.debug(f"Recommendations: {recommendations}")

#     return jsonify({'recommendations': recommendations})

# if __name__ == "__main__":
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(host='0.0.0.0', port=8080, debug=True)


# from flask import Flask, render_template, request, jsonify
# import tensorflow as tf
# from keras.models import load_model
# from keras.preprocessing import image
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.preprocessing import StandardScaler
# import numpy as np
# import pandas as pd
# import os
# import base64
# from PIL import Image
# import io
# import logging

# app = Flask(__name__)
# app.secret_key = b'\x93\x1f\xd7\xae\x92\xb2\xdd\xf7\xcbk\xc1e\xbf\x12\xd5M\xd3\x17v\xd9\x8fUj\xf7'  # Replace with your generated key

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)

# # Load the trained MobileNet model
# model_path = 'models/my_model.h5'  # Adjust the path if necessary
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     raise FileNotFoundError(f"Model file not found at {model_path}")


# # reading the data from dataset
# products_df = pd.read_csv('preprocessed_dataset_products.csv')

# # Define a function to preprocess the image from file path
# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# # Define a function to preprocess the image from base64 data
# def preprocess_image_from_base64(base64_str):
#     img = Image.open(io.BytesIO(base64.b64decode(base64_str))).convert('RGB')
#     img = img.resize((150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0
#     return img_array

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' in request.files and request.files['file'].filename != '':
#         file = request.files['file']
#         file_path = os.path.join('uploads', file.filename)
#         file.save(file_path)
        
#         # Preprocess the image
#         img_array = preprocess_image(file_path)
#     elif 'image_data' in request.form:
#         base64_image = request.form['image_data']
#         img_array = preprocess_image_from_base64(base64_image)
#     else:
#         return jsonify({'error': 'No image provided'}), 400
    
#     # Make a prediction
#     prediction = model.predict(img_array)
#     predicted_class = np.argmax(prediction, axis=1)[0]
    
#     # Map predicted class index to class name (adjust based on your class indices)
#     class_indices = {0: 'Acne', 1: 'Clear Skin', 2: 'Comedone'}  # Replace with your actual class names
#     result = class_indices.get(predicted_class, 'Unknown Condition')
    
#     return jsonify({'prediction': result})

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     form_data = request.form.to_dict()
#     user_features = np.array([[float(value) for value in form_data.values()]])

#     scaler = StandardScaler()
#     scaled_features = scaler.fit_transform(products_df.iloc[:, 3:])

#     similarity_scores = cosine_similarity(scaled_features, user_features)
#     top_indices = np.argsort(similarity_scores.flatten())[-5:][::-1]

#     recommendations = products_df.iloc[top_indices][['Product', 'product_url']].to_dict(orient='records')

#     return jsonify({'recommendations': recommendations})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import os
import base64
from PIL import Image
import io
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Replace with your email configuration
EMAIL_ADDRESS = 'padmasree.91004@gmail.com'
EMAIL_PASSWORD = 'tiaf lkln xdyv mgvg '
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Load the trained MobileNet model

app = Flask(__name__)

# Load the trained model
model_path = 'models/my_model.h5'  # Adjust the path if necessary
if os.path.exists(model_path):
    model = load_model(model_path)
else:
    raise FileNotFoundError(f"Model file not found at {model_path}")


# reading the data from dataset
dataf = pd.read_csv('preprocessed_dataset_products.csv')
# Define a function to preprocess the image from file path
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Define a function to preprocess the image from base64 data
def preprocess_image_from_base64(base64_str):
    img = Image.open(io.BytesIO(base64.b64decode(base64_str))).convert('RGB')
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array
# Define the unique feature columns
feature_columns = [
    'Combination', 'Dry', 'Oily', 'Sensitive','Acne'
# Define the unique feature columns
feature_columns = [
    'Combination', 'Dry', 'Oily', 'Sensitive', 'Acne', 'Irritation',
    'Broken barrier', 'Dark Spots', 'Exfoliation', 'Hydration',
    'Pigmentation', 'Pimples', 'Pores', 'Skin soothing', 'Sun protection',
    'Whitehead/Blackhead'
]
# Strip leading and trailing spaces from column names
dataf.columns = dataf.columns.str.strip()
# Ensure 'Product' column is string type
dataf['Product'] = dataf['Product'].astype(str)
# Define features and product names
features = dataf[feature_columns]
product_names = dataf['Product']

# Normalize the feature data
scaler = StandardScaler()
normalized_features = scaler.fit_transform(features)
# Get the product names
product_names = dataf['Product']
def get_user_profile(skin_condition,form_data):
    # Extract user input from form data
    user_input = {column: int(form_data.get(column, 0)) for column in feature_columns}
    
        # Include the skin condition prediction
    if skin_condition == 'ACNE':
        user_input['Acne'] = 1
    else:
        user_input['Acne'] = 0
def get_user_profile(form_data):
    # Extract user input from form data
    user_input = {column: int(form_data.get(column, 0)) for column in feature_columns}
    # Create a DataFrame from the user input
    user_profile = pd.DataFrame([user_input], columns=features.columns)

    # Normalize the user profile using the same scaler
    normalized_user_profile = scaler.transform(user_profile)

    return normalized_user_profile


def recommend_products(normalized_user_profile, normalized_features, product_names, top_n=3):
    # Compute cosine similarity between user profile and all products
    user_sim = cosine_similarity(normalized_user_profile, normalized_features)

    # Get the top N most similar products
    top_indices = user_sim[0].argsort()[-(top_n+1):][::-1][1:]  # Skip the first one as it will be the user profile itself

    # Get the product names of the top N recommendations
    recommended_products = product_names.iloc[top_indices]

    return recommended_products

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/recommendation')
def recommendation_page():
    return render_template('recommendation.html')


@app.route('/consultation')
def consultation_page():
    return render_template('consultation.html')

@app.route('/products')
def products_page():
    return render_template('product_details.html')

# Define a function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Define a function to preprocess the image from base64 data
def preprocess_image_from_base64(base64_str):
    img = Image.open(io.BytesIO(base64.b64decode(base64_str)))
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Preprocess the image
        img_array = preprocess_image(file_path)
    elif 'image_data' in request.form:
        base64_image = request.form['image_data']
        img_array = preprocess_image_from_base64(base64_image)
    else:
        return jsonify({'error': 'No image provided'}), 400
    
    # Make a prediction
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Debugging: print prediction and predicted_class
    print(f'Prediction: {prediction}, Predicted class: {predicted_class}')
    
    # Map predicted class index to class name (adjust based on your class indices)
    class_indices = {0: 'ACNE', 1: 'CLEAR SKIN', 2: 'COMEDONE'}  # Replace with your actual class names
    result = class_indices.get(predicted_class, 'UNKNOWN CONDITION')
    
    # Debugging: print result
    print(f'Result: {result}')

    
    # Map predicted class index to class name (adjust based on your class indices)
    class_indices = {0: 'Acne', 1: 'Clear Skin', 2: 'Comedone'}  # Replace with your actual class names
    result = class_indices.get(predicted_class, 'Unknown Condition')
    
    return jsonify({'prediction': result})

@app.route('/recommend', methods=['POST'])
def recommend():

    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Preprocess the image
        img_array = preprocess_image(file_path)
    elif 'image_data' in request.form:
        base64_image = request.form['image_data']
        img_array = preprocess_image_from_base64(base64_image)
    else:
        return jsonify({'error': 'No image provided'}), 400
    
    # Make a prediction
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    # Map predicted class index to class name
    class_indices = {0: 'ACNE', 1: 'CLEAR SKIN', 2: 'COMEDONE'}  # Replace with your actual class names
    skin_condition = class_indices.get(predicted_class, 'UNKNOWN CONDITION')
    
    # Create user profile and get recommendations based on the predicted skin condition
    user_profile = get_user_profile(skin_condition, request.form)
    recommended_products = recommend_products(user_profile, normalized_features, product_names, top_n=3)
    return jsonify({'recommendations': recommended_products.tolist()})




@app.route('/consult', methods=['POST'])
def consult():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # Log the consultation request to console (for testing purposes)
    print(f"Consultation request received from {name} ({email}, {phone}): {message}")

    # Send the consultation request via email (or handle it as needed)
    try:
        send_email(name, email, phone, message)
        response = {"message": "Your consultation request has been sent successfully!"}
        status_code = 200
    except Exception as e:
        print(f"Error sending email: {e}")
        response = {"message": "There was an error sending your consultation request. Please try again later."}
        status_code = 500

    return jsonify(response), status_code
def send_email(name, email, phone, message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = 'New Consultation Request'

    body = f"""
    You have received a new consultation request from:

    Name: {name}
    Email: {email}
    Phone: {phone}
    Message:
    {message}
    """
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, text)
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
    form_data = request.form
    user_profile = get_user_profile(form_data)
    recommended_products = recommend_products(user_profile, normalized_features, product_names, top_n=3)
    
    return jsonify({'recommendations': recommended_products.tolist()})

if __name__ == "_main_":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(host='0.0.0.0', port=8080, debug=True)
