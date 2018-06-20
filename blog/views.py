from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Question
from django.views.generic import DetailView, ListView
from django.db.models import Q
from taggit.models import Tag


# Create your views here.

class QuestionListView(ListView):
    model = Question
    def get_queryset(self):
        return Question.objects.all()


def question_detail(request, slug):
    question = get_object_or_404(Question, slug = slug)
    question.hits = question.hits + 1
    question.save()
    
    # Get 3 news question
    related_question = Question.objects.all().order_by('-create_date')[:3]
    tag_cloud = Tag.objects.all()
    context = {
        "question": question,
        'related_question': related_question,
        'tags' : tag_cloud
    }

    return render(request, "blog/post-detail.html", context=context)

def index(request):
    query = request.GET.get("q")
    tags = Tag.objects.all()
    question_list= []
    if query:
        question_list = Question.objects.all()
        # get_query()
        question_list = question_list.filter(
            Q(title__icontains = query)
        ).distinct()
        context = {
            'question_list': question_list,
        }
        return render(request, 'blog/search_result.html', context = context)
    else:
        question_list = Question.objects.all()[:3]
    context = {
        "question_list": question_list,
        "query": query,
    }

    return render(request, 'blog/homepage.html', context = context)
