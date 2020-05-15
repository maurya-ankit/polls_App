from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


@login_required(login_url='register:signin')
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('id')
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not Exist")
#     return render(request, 'polls/detail.html', {'question': question})

# an efficient way to do it
@login_required(login_url='register:signin')
def detail(request, question_id ):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required(login_url='register:signin')
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required(login_url='register:signin')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@login_required(login_url='register:signin')
def about(request):
    return render(request, 'polls/about.html')


# def signup(request):
#     return render(request, 'polls/signup.html')
#
# def signin(request):
#     return render(request, 'polls/../register/templates/register/SignIn.html')
