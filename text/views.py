from django.shortcuts import render
from django.views.generic import FormView
from text.models import TextNews
from .forms import RegisterForm

def home_page(request):
    news = TextNews.objects.order_by('id')
    # news = TextNewsModel.objects.values_list('title_name')
    context = {'news': news}
    return render(request,template_name='index.html',context=context)

class MyFormView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login'