from models.model import FoodRecognitionModel
from data.dataset_loader import DatasetLoader
from data.preprocess import preprocess_image
from utils.logger import Logger
from inference.predict import predict_food

def main():
    logger = Logger()
    logger.log_info("Starting Food Image Recognition Application")

    # Load the dataset
    dataset_loader = DatasetLoader()
    data, labels = dataset_loader.load_data()
    logger.log_info("Data loaded successfully")

    # Preprocess the images
    preprocessed_data = [preprocess_image(image) for image in data]
    logger.log_info("Images preprocessed successfully")

    # Initialize and load the model
    model = FoodRecognitionModel()
    model.build_model()
    model.compile_model()
    logger.log_info("Model built and compiled successfully")

    # Example of predicting food item from an image
    # Replace 'path_to_image' with the actual image path
    image_path = 'path_to_image'
    prediction = predict_food(image_path, model)
    logger.log_info(f"Predicted food item: {prediction}")

if __name__ == "__main__":
    main()