from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex) /polls/
    path('', views.index, name='index'),
    # ex) /polls/1/
    # <>괄호안에 해당하는 값을 뷰에 인자로 전달
    path('<int:question_id>/', views.detail, name='detail'),
    # ex) /polls/1/result/
    path('<int:question_id>/result/', views.result, name='result'),
    # ex) /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]