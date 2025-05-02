# Food Image Recognition Project

This project implements an image recognition system to identify food items in images using deep learning techniques. The system is designed to load a dataset of food images, preprocess the images, train a neural network model, and make predictions on new images.

## Project Structure

```
food-image-recognition
├── src
│   ├── main.py                # Entry point of the application
│   ├── data
│   │   ├── dataset_loader.py   # Class for loading and processing the dataset
│   │   └── preprocess.py       # Functions for image preprocessing
│   ├── models
│   │   ├── model.py            # Defines the neural network model
│   │   └── train.py            # Class for training and evaluating the model
│   ├── utils
│   │   ├── image_utils.py      # Utility functions for image handling
│   │   └── logger.py           # Logger class for logging information and errors
│   └── inference
│       └── predict.py          # Function for making predictions on images
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files and directories to ignore in Git
├── README.md                   # Project documentation
└── tests
    ├── test_dataset_loader.py   # Unit tests for DatasetLoader
    ├── test_model.py            # Unit tests for FoodRecognitionModel
    └── test_predict.py          # Tests for predict_food function
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd food-image-recognition
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare your dataset of food images and update the dataset loading paths in `src/data/dataset_loader.py`.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the prompts to input the image file path for recognition.

## Examples

- Place an image of food in the specified directory and run the application to see the predicted food item.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.