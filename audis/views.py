from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import ChoiceQuestion, TextQuestion

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username= username, password=password)

        if user is not None:
            auth.login(request,user)
            
            return redirect('questions')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect( '/')
    
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method== 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
        

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already Used')           
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register') 
            
            else:
                user = User.objects.create_user(username=username, email=email, password= password)
                user.save(); ######## I DON'T SEE THE POINT OF THE ; USED HERE
                return redirect('login')
        else:
            messages.info(request, 'Password confirmation failed')
            return redirect('register')
    else:
        return render(request, 'login.html')

def questions(request):
    current_user = request.user
    questions= TextQuestion.objects.filter(question_user__isnull= True)

    for i in range(1,len(questions)+1):
        response = "response"+str(i)
        if response in request.POST:
            new_question_text=questions[i-1].question_text
            new_text_response= request.POST[response]
            new_question_user = current_user
            ques = TextQuestion.objects.create(question_text=new_question_text, question_response=new_text_response, question_user=new_question_user)
            ques.save();
        else:
            pass
    
    # choicequestions = ChoiceQuestion.objects.filter(question_user__isnull=True)
    

    if request.method=='POST':
        new_choice_question_text= "Which teams do you want to audition for?"
        new_choice_question_user= current_user
        new_choice_question_response= request.POST['responsechoice']

        new_choice_question = ChoiceQuestion.objects.create(question_text=new_choice_question_text,question_user=new_choice_question_user, question_response=new_choice_question_response)
        new_choice_question.save();
    else:
        pass





            

    
    
    context={
        'questions':questions,
        'user':current_user,
        
        

    }
    return render(request, 'Audition Form.html', context)
    
