import unittest
from src.models.model import FoodRecognitionModel

class TestFoodRecognitionModel(unittest.TestCase):

    def setUp(self):
        self.model = FoodRecognitionModel()

    def test_model_architecture(self):
        model = self.model.build_model()
        self.assertIsNotNone(model)

    def test_model_compilation(self):
        model = self.model.build_model()
        compiled_model = self.model.compile_model(model)
        self.assertIsNotNone(compiled_model)

if __name__ == '__main__':
    unittest.main()