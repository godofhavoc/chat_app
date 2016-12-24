from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from chat.models import Messages
from django.contrib.auth import logout

# Create your views here.
def chat_login(request):

    # import pdb; pdb.set_trace()

    return render(request, "chat/login.html", {})

def chat_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def chat_room(request):
    # room, created = Room.objects.get_or_create(label=label)
    messages = reversed(Messages.objects.order_by('-timestamp')[:50])

    return render(request, "chat/room.html", {
        # 'room': room,
        'messages': messages,
    })
