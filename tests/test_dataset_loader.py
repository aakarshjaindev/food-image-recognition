import unittest
from src.data.dataset_loader import DatasetLoader

class TestDatasetLoader(unittest.TestCase):

    def setUp(self):
        self.loader = DatasetLoader(data_dir='path/to/data')

    def test_load_data(self):
        images, labels = self.loader.load_data()
        self.assertIsInstance(images, list)
        self.assertIsInstance(labels, list)
        self.assertGreater(len(images), 0)
        self.assertEqual(len(images), len(labels))

    def test_get_labels(self):
        labels = self.loader.get_labels()
        self.assertIsInstance(labels, list)
        self.assertGreater(len(labels), 0)

if __name__ == '__main__':
    unittest.main()