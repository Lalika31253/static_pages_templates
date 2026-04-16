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
  pass