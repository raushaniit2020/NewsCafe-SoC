from turtle import title
from urllib import response
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests
from django.shortcuts import HttpResponse 

api_key='98e33e75684f4c268717fa4f1fe00d20'

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home(request):
    api_url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}'
    response=requests.get(api_url)
    data_as_json=response.json()  
    data_articles=data_as_json['articles']
    dict1={'data_articles':data_articles}
    # source=[]
    # author=[]
    # title=[]
    # description=[]
    # date=[]
    # url=[]
    # for i in data_articles:

    #     author.append(i['author'])
    #     source.append(i['source']['name']) 
    #     date.append(i['publishedAt'])
    #     url.append(i['url'])
    #     description.append(i['description'])
    #     title.append(i['title'])


    # news=zip(author, title, description, source, date, url)
    return render(request, 'home.html', dict1)


def search(request):
    search=request.GET.get('search')
    api_url=f'https://newsapi.org/v2/everything?q={search}&from=2022-04-25&sortBy=publishedAt&apiKey={api_key}'
    response=requests.get(api_url)
    data_as_json=response.json()  
    data_articles=data_as_json['articles']
    dict1={'data_articles':data_articles}
    return render(request, 'search.html', dict1)

    
