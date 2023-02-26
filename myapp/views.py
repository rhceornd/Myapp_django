from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import Post
from django.utils import timezone

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'myapp/post_list.html', {'posts' : posts})
