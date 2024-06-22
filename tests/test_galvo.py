import unittest
from quantum_control.hardware.galvo_mirror import GalvoMirror

class TestGalvoMirror(unittest.TestCase):
    def test_move_to(self):
        galvo = GalvoMirror('Dev1', 'ao0', 'ao1')
        galvo.move_to(0.5, 0.5)
        # Add assertions and mock checks as needed
        galvo.close()

if __name__ == '__main__':
    unittest.main()
