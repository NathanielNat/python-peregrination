from survey import AnonymousSurvey

# define question  and make survey 
question = 'What language did you first learn to speak ?'

my_survey  = AnonymousSurvey(question)

#show question and store responses to question 

my_survey.show_question()

print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q' :
        break
    my_survey.store_response(response)


#show survey result
print('\n Thank you to everyone who participated in this !')
my_survey.show_results()


