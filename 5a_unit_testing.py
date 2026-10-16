from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for positive sentiment
        result = emotion_detector("I love working with Python")
        self.assertTrue(not None in result.values(), f" There is a 'None' within the values of: {result}")

    def test_emotion_detector_with_arg_as_none(self):
        # Test case for positive sentiment
        result = emotion_detector(None)
        self.assertTrue(None in result.values(), f" There is not a 'None' within the values of: {result}")

    def test_emotion_detector_with_arg_as_empty(self):
        # Test case for positive sentiment
        result = emotion_detector('')
        self.assertTrue(None in result.values(), f" There is not a 'None' within the values of: {result}")
        result = emotion_detector("")
        self.assertTrue(None in result.values(), f" There is not a 'None' within the values of: {result}")

unittest.main()
