from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from chat.models import Messages, ResortDocument
from django.contrib.auth import logout
from django.core.files.base import ContentFile
import os

from googleapiclient.discovery import build

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

def upload_resorts(request):

    if request.method == 'POST':
        resort_list = request.FILES['input_file']
        country_name = os.path.splitext(resort_list.name)[0]

        for line in resort_list:
            new_file = ContentFile('')
            resort_name = line.decode('utf-8').rstrip()
            query = resort_name + ' ' + country_name

            service = build("customsearch", "v1",
            developerKey=os.environ['GOOGLE_API'])

            res = service.cse().list(
                q = query,
                cx = os.environ['CX'],
                num = 10,
                searchType = 'image'
            ).execute()

            for item in res['items']:
                new_file.write('%s\n' % item['link'])

            resort_obj = ResortDocument.objects.create(place=country_name)
            resort_obj.document.save(resort_name + '.txt', new_file)
            resort_obj.save()



    return render(request, 'chat/upload.html', {})
