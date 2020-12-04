import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """create a survey and setup responses for user in all test methods"""
        question = 'What language did you learn to speak first?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Ewe','English','Python']

 
    """Test for Anonymous survey"""
    def test_store_single_response(self):
        """Test that a single response is stored"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)


    def test_store_three_reponses(self):
        """test that three responses are properly stored """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)




if __name__ == '__main__':
    unittest.main()
