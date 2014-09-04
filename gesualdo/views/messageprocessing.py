from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from gesualdo.models.message import Message
from gesualdo.models.piece import Piece
from gesualdo.models.userprofile import UserProfile

def addComment(request):
    message = request.POST.get("message")
    piece = Piece.objects.get(pk=request.POST.get("piece"))
    measure = request.POST.get("measure")
    voice = request.POST.get("voice")
    if request.user.is_authenticated():
        try:
            user_post = request.user.userprofile
        except UserProfile.DoesNotExist:
            user_post = None
    else:
        user_post = None
    ip = get_client_ip(request)
    if request.method == 'POST':
        if 'file' in request.FILES:
            com = Message(user_post=user_post, message=message, piece=piece, voice=voice, measure=measure, ip=ip, file=request.FILES['file'])
        else:
            com = Message(user_post=user_post, message=message, piece=piece, voice=voice, measure=measure, ip=ip)
    else:
        com = Message(user_post=user_post, message=message, piece=piece, voice=voice, measure=measure, ip=ip)
    com.save()
    return HttpResponse(com.id);
    

def validateComment(request):
    if request.user.has_perm("validate_message"):
        com = Message.objects.get(pk=request.POST.get('id'))
        com.validated = True
        com.save()
        return HttpResponse(request.POST.get('id'))
    else:
        return HttpResponse("-1")

def refuseComment(request):
    if request.user.has_perm("validate_message"):
        com = Message.objects.get(pk=request.POST.get('id'))
        com.delete()
        return HttpResponse(request.POST.get('id'))
    else:
        return HttpResponse("-1")

def archiveComment(request):
    if request.user.has_perm("archive_message"):
        com = Message.objects.get(pk = request.POST.get('id'))
        com.archived = True
        com.save()
        return HttpResponse(request.POST.get('id'))
    else:
        return HttpResponse("-1")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
