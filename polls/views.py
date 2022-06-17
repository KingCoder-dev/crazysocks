from asyncore import poll
from django.shortcuts import render, redirect

from .forms import imageForm

from .models import *

# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def polls_view(request):
    qs = Polls.objects.all()

    context = {
        'qs': qs,

    }
    return render(request, 'polls/polls.html', context)


def like_poll(request):
    ip = get_client_ip(request)
    if request.method == 'POST':
        poll_id = request.POST.get('poll_id')
        poll_obj = Polls.objects.get(id=poll_id)
        if not IpModel.objects.filter(ip=ip).exists():
            IpModel.objects.create(ip=ip)

        if poll_obj.liked.filter(id=IpModel.objects.get(ip=ip).id).exists():
            poll_obj.liked.remove(IpModel.objects.get(ip=ip))
        else:
            poll_obj.liked.add(IpModel.objects.get(ip=ip))
        return redirect('polls:poll-list')


def upload(request):
    form = imageForm()
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('polls:poll-list')
    context = {'form': form}
    return render(request, 'polls/upload.html', context)
