from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Question



class IndexView(ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        
        return Question.objects.order_by('-pub_date')[:5]

class DetailsView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(DetailView):
    model = Question
    template_name = 'polls/result.html'