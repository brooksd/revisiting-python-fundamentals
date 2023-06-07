quiz = {
    "Q1": {
        'question': 'What is the capital of France?',
        'answer': 'Paris'       
    },
    "Q2": {
        'question': 'What is the capital of Kenya?',
        'answer': 'Nairobi'       
    },
    "Q3": {
        'question': 'What is the capital of Uganda?',
        'answer': 'Kampala'       
    },
    "Q4": {
        'question': 'What is the capital of United Kingdom?',
        'answer': 'London'       
    },
    "Q5": {
        'question': 'What is the capital of South Africa?',
        'answer': 'Johannesburg'       
    },
    "Q6": {
        'question': 'What is the capital of United States?',
        'answer': 'Washington DC'       
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score = score + 1
        print('Your score is: ' + str(score))
        
    else:
        print('Wrong!')
        print('The answer is : ' + value['answer'])
        print('Your score is: ' + str(score))