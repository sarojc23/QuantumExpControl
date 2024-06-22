import unittest
from quantum_control.hardware.photodiode import Photodiode

class TestPhotodiode(unittest.TestCase):
    def test_photodiode_measurement(self):
        photodiode = Photodiode('Dev1', 'ai0')
        photodiode.start_measurement()
        data = photodiode.read_data()
        self.assertIsNotNone(data)
        photodiode.stop_measurement()

if __name__ == '__main__':
    unittest.main()
