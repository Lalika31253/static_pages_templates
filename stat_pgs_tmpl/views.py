from django.shortcuts import render

def home(request):
    ctx = {
        'name': "ComIT",
        'students': 10,
        'names': ["Bob", "Sarah", "Don", "Inna", "Alex", "Tim", "Greg", "Anna", "Ryan", "Sam"],
        'is_active': True
    }
    return render(request, 'stat_pgs_tmpl/home.html', ctx)


def contact(request):
  ctx = {
     'medias': ["Facebook", "LinkedIn", "Instagram", "Telegram"]
  }
  return render(request, 'stat_pgs_tmpl/contact.html', ctx)

def about(request):
    return render(request, 'stat_pgs_tmpl/about.html')