from django.shortcuts import render
from pages.models import *
from django.http import JsonResponse
from django.contrib.auth.models import User


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'pro': projects})


def send_message(request):
    if request.method == 'POST':
        msg = Message()
        msg.sender = request.user
        msg.recipient = User.objects.get(username=request.POST.get('recipient'))
        msg.project = Project.objects.get(title=request.POST.get('project_name'))
        cast = request.POST.get('cast_id')
        if cast:
            msg.cast = Cast.objects.get(pk=cast)

        crew = request.POST.get('crew_id')
        if crew:
            msg.crew = Cast.objects.get(pk=crew)

        msg.body = request.POST.get('message_body')
        msg.save()
        return JsonResponse({'message': 'Success'})
    return JsonResponse({'message': 'Request must be post.'})


def view_received_message(request):
    return render(request, 'view_received_message.html')


def view_single_message(request, slug):
    message = Message.objects.get(pk=slug)
    message.read = True
    message.save()
    return render(request, 'view_single_message.html', {'message': message})
