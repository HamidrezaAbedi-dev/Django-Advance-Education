from django.shortcuts import render

# Create your views here.

def indexView(request):
    title = 'fbv'
    name = 'hamid'
    context = {'name':name, 'title':title}
    return render(request, 'index.html', context)