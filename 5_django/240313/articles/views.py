from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'class_name':'서울1반',
        'arr':['가','나','다'],
        'dict':{'A':10},
    }
    return render(request,'articles/index.html',context)