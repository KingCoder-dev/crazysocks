from asyncore import poll
from django.shortcuts import render, redirect

from .models import *

# Create your views here.


def polls_view(request):
    qs = Polls.objects.all()
    user = request.user
    context = {
        'qs': qs,
        'user': user
    }
    return render(request, 'polls/polls.html', context)


def like_poll(request):
    user = request.user
    if request.method == 'POST':
        poll_id = request.POST.get('poll_id')
        poll_obj = Polls.objects.get(id=poll_id)

        if user in poll_obj.liked.all():
            poll_obj.liked.remove(user)
        else:
            poll_obj.liked.add(user)
    return redirect('polls:poll-list')
