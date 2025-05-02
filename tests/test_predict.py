import pytest
from src.inference.predict import predict_food

def test_predict_food_valid_image():
    # Test with a valid image path
    image_path = 'tests/images/test_food.jpg'  # Replace with a valid test image path
    prediction = predict_food(image_path)
    assert prediction in ['pizza', 'burger', 'salad', 'sushi']  # Replace with actual food items

def test_predict_food_invalid_image():
    # Test with an invalid image path
    image_path = 'tests/images/invalid_image.jpg'
    prediction = predict_food(image_path)
    assert prediction is None  # Expecting None for invalid images

def test_predict_food_empty_image():
    # Test with an empty image path
    image_path = ''
    prediction = predict_food(image_path)
    assert prediction is None  # Expecting None for empty image path

def test_predict_food_non_image_file():
    # Test with a non-image file
    image_path = 'tests/files/test_text.txt'  # Replace with a valid non-image file path
    prediction = predict_food(image_path)
    assert prediction is None  # Expecting None for non-image files