from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class TextQuestion(models.Model):
    question_text= models.CharField(max_length= 500, null = True, blank = False)
    question_response=models.CharField(max_length=3000, null= True, blank= True)
    question_user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return (str(self.question_text)+"   ::::   "+str(self.question_user))

class ChoiceQuestion(models.Model):
    # choices=[
    #     ('Core','Core'),
    #     ('Tech','Tech'),
    #     ('Both Core and Tech', 'Both Core and Tech')
    # ]
    question_text= models.CharField(max_length=500, null = True, blank = False)
    question_response= models.CharField(max_length=100, blank=True, null=True)
    question_user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return (str(self.question_text)+"  ::::   "+str(self.question_user))

class CoreTeamQuestions(models.Model):
    pass


