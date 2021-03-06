import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    """Test for Anonymous survey"""
    def test_store_single_response(self):
        """Test that a single response is stored"""
        question = 'What language did you learn to speak first?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Ewe')
        self.assertIn('Ewe',my_survey.responses)


    def test_store_three_reponses(self):
        """test that three responses are properly stored """
        question = 'What language did you learn to speak first?'
        my_survey = AnonymousSurvey(question)
        responses = ['Ewe','English','Ga']
        for response in responses:
            my_survey.store_response(response)




if __name__ == '__main__':
    unittest.main()
