from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

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
    # 파일이 존재하지 않을 때 발생하는 404오류
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')

    # Http404를 처리할 때 loader-render 관계처럼(render) 단축 함수가 존재(get_object_or_404)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def result(request, question_id):
    response = "You're looking ah the results of queston %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're votiong on question %s" %question_id)
