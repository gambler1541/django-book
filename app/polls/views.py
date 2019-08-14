from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    # render 메서드는 request와 템플릿 이름, 사전형 객체(context)를 인자로 받음
    #   사전형 객체는 템플릿에서 사용할 변수
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking ah question %s." %question_id)

def result(request, question_id):
    response = "You're looking ah the results of queston %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're votiong on question %s" %question_id)
