from django.shortcuts import render

def home(request):
    ctx = {
        "theme": "cupcake",
        "name": "ComIT",
        "students": 10,
        "names": ["Bob", "Sarah", "Don", "Inna", "Alex", "Tim", "Greg", "Anna", "Ryan", "Sam"],
        "is_active": True
    }
    return render(request, 'stat_pgs_tmpl/home.html', ctx)


def contact(request):
  ctx = {
     "theme": "retro",
     "medias": ["Facebook", "LinkedIn", "Instagram", "Telegram"]
  }
  return render(request, 'stat_pgs_tmpl/contact.html', ctx)


def about(request):
    ctx = {
        "theme": "valentine"
    }
    return render(request, 'stat_pgs_tmpl/about.html', ctx)


def news(request):
    ctx = {
        "theme": "caramellatte",
        "news": ["February", "March", "April"]
    }
    return render(request, 'stat_pgs_tmpl/news.html', ctx)