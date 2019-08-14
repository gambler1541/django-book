from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking ah question %s." %question_id)

def result(request, question_id):
    response = "You're looking ah the results of queston %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're votiong on question %s" %question_id)
