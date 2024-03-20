from django.shortcuts import render
from .models import Poll, Choice

def index(request):
    polls = Poll.objects.all()
    return render(request, 'touch polls/index.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    return render(request, 'polls/touch poll_detail.html', {'poll': poll})

def poll_create(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        poll = Poll.objects.create(question=question, created_by=request.user)
        return render(request, 'polls/touch poll_detail.html', {'poll': poll})
    return render(request, 'polls/touch poll_create.html')

def poll_update(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        question = request.POST.get('question')
        poll.question = question
        poll.save()
        return render(request, 'polls/touch poll_detail.html', {'poll': poll})
    return render(request, 'polls/touch poll_update.html', {'poll': poll})

def poll_delete(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    poll.delete()
    return render(request, 'polls/touch poll_delete.html')
