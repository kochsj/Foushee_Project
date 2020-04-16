from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def homePageView(request):
#     return HttpResponse("Welcome")

# class HomePageView(TemplateView):
#     template_name = 'newsfeed.html'

def newsfeed_view(request):

    context = {}
    context['authorized'] = True

    list_of_news = []
    list_of_news.append("News article one")
    list_of_news.append("News article two")
    list_of_news.append("News article three")
    list_of_news.append("News article four")

    context['list_of_news'] = list_of_news

    return render(request, "newsfeed.html", context)
