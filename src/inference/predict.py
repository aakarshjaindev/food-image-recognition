def predict_food(image_path):
    import numpy as np
    from tensorflow.keras.models import load_model
    from src.utils.image_utils import load_image, preprocess_image

    # Load the trained model
    model = load_model('path/to/your/trained_model.h5')

    # Load and preprocess the image
    image = load_image(image_path)
    processed_image = preprocess_image(image)

    # Make prediction
    predictions = model.predict(np.expand_dims(processed_image, axis=0))
    predicted_class = np.argmax(predictions, axis=1)

    # Map predicted class to food item (this mapping should be defined based on your dataset)
    food_items = ['pizza', 'burger', 'sushi', 'salad']  # Example food items
    return food_items[predicted_class[0]]