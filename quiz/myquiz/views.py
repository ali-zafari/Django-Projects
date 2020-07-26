from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import QuestionBank
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def send_questions(request):
    """
    on the 'GET' method, it will send the questions with possible choices to user
    
    input: nothing
    output: json including questoins and choices
    """
    if request.method == 'GET':
        columns_to_print = ['id', 'question','choice1','choice2','choice3','choice4']
        questions = list(QuestionBank.objects.all().values(*columns_to_print))
        return JsonResponse(questions, safe=False)
    else:
        return HttpResponse('Please use "GET" method only.')


@csrf_exempt
def calculate_score(request):
    """
    on the 'POST' method, it will send the user's score to her/him
    
    input: json including the users answers
    output: json including the user's score
    """
    if request.method == 'POST':
        answers_dict = json.loads(request.body)
        wrong_ans = 0
        true_ans = 0
        for qid, answer in answers_dict.items():
            try:
                if int(answer) == QuestionBank.objects.values().get(id=qid)['answer']:
                    true_ans += 1
                else:
                    wrong_ans += 1
            except:
                pass
        score = (true_ans*3- wrong_ans)/(20*3)*100
        return JsonResponse({"Your Score": f"{score} %"})
    else:
        return HttpResponse('Please use "POST" method only.')


@csrf_exempt
def add_question(request):
    """
    on the 'POST' method, it wil add a question to our database

    input: json including a question, its four choices and the right answer
    output: nothing
    """
    if request.method == 'POST':
        data_dict = json.loads(request.body)
        for _, question in data_dict.items():
            question_to_add = QuestionBank(**question)
            question_to_add.save()
        return HttpResponse(f'The following question(s) has been added to DB successfully:\n{data_dict}')
    else:
        return HttpResponse('Please use "POST" method only.')