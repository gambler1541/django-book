import datetime

from django.db import models
from django.utils import timezone




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # 사람이 읽기 쉬운 형태를 사용하기 위해 인자로 문자열 전달
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    # __str__함수는 관리자 화면이나 쉘에서 객체를 출력할 때 나타날 내용을 결정
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


