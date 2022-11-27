from django.shortcuts import render

# Create your views here.

def home(req):
    return render(request=req, template_name='home/index.html')

def riddle(req):
    # Напиши свой прекрасный код сюда, чтобы выводилась страничка с загадкой

    pass

def answer(req):
    # Напиши свой прекрасный код сюда, чтобы выводилась страничка с ответом на загадку

    pass

def multiply(req):
    ctx = {}
    ctx['values'] = []
    
    # Напиши свой прекрасный код сюда, чтобы генерировалась таблица умножения для числа 5
    
    return render(request=req, template_name='multiply/multiply.html', context=ctx) 