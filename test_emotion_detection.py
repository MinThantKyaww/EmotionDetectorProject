"""Integration tests for the Watson emotion detector."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Check the dominant emotion for five example sentences."""

    def test_dominant_emotions(self):
        """Check each emotion with an example sentence."""
        examples = (
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        )
        for sentence, expected in examples:
            with self.subTest(sentence=sentence):
                result = emotion_detector(sentence)
                self.assertEqual(result["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
