import unittest
from utils import extract_keywords, match_score

class TestUtils(unittest.TestCase):

    def test_extract_keywords(self):
        resume_text = "I am a software developer with experience in Python and Machine Learning."
        expected_keywords = ['software', 'developer', 'experience', 'python', 'machine', 'learning']
        extracted_keywords = extract_keywords(resume_text)

        for keyword in expected_keywords:
            self.assertIn(keyword, extracted_keywords, f"Keyword '{keyword}' not found in extracted keywords.")

    def test_match_score(self):
        resume_keywords = ['python', 'developer', 'machine', 'learning']
        job_description_keywords = ['python', 'machine', 'learning', 'developer']
        score, common_keywords = match_score(resume_keywords, job_description_keywords)

        self.assertEqual(score, 100, f"Expected match score of 100, but got {score}.")
        self.assertListEqual(common_keywords, ['python', 'developer', 'machine', 'learning'],
                             f"Expected common keywords ['python', 'developer', 'machine', 'learning'], but got {common_keywords}.")

if __name__ == "__main__":
    unittest.main()
