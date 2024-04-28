from django.shortcuts import render

from text.models import TextNews

def home_page(request):
    news = TextNews.objects.order_by('id')
    # news = TextNewsModel.objects.values_list('title_name')
    context = {'news': news}
    return render(request,template_name='index.html',context=context)
