class AnonymousSurvey:
    """collect annonymous answers to a survey question"""   
    def __init__(self,question):
        """Store a question, and prepare to store responses."""
        self.question  = question
        self.responses = []

    def show_question(self):
        """print survey question"""
        print(self.question)
    
    def store_response(self,new_response):
        """Store a single response to a survey """
        self.responses.append(new_response)

    def show_results(self):
        """show all the responses given """
        print('Survey results: ')
        for response in self.responses:
            print(f'- {response}')