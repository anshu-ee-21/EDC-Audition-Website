from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class TextQuestion(models.Model):
    question_text= models.CharField(max_length= 500, null = True, blank = False)
    question_response=models.CharField(max_length=3000, null= True, blank= True)
    question_user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.question_text
        