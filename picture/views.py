

import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Article
from django.shortcuts import render,redirect


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/todays-news.html', {"date": date,"news":news})

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})
  

def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})
    
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Pixel.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'locations/search.html',{"message":message,"pixel": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

