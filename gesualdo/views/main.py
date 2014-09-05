from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gesualdo.models.text import Text
from gesualdo.models.book import Book
from gesualdo.models.book_copy import BookCopy
from gesualdo.models.piece import Piece
from gesualdo.models.message import Message
from gesualdo.models.person import Person

def home(request):
    return render(request, 'main/home.html')

def book(request, pk):

    book = Book.objects.get(book_id=pk)
    mainsource = BookCopy.objects.filter(book_id=pk)
    """othersources = BookCopy.objects.filter(book_id=pk)"""
    pieces = Piece.objects.filter(mainsource=mainsource)

    othereditions = book.other_editions.all()

    return render(request, 'main/book.html', {'book': book, 'mainsource':mainsource, 'pieces':pieces, 'othereditions': othereditions})


def books(request):
    books = Book.objects.all().order_by('id') 

    return render(request, 'main/books.html', {'books': books})

def piece(request, book, place):
    try:
        sources = BookCopy.objects.filter(book_id=(Book.objects.get(book_id=book)))
        piece = Piece.objects.get(mainsource__in=sources, book_position=place)
        comments = []
        ip = get_client_ip(request)
        print ip
        if request.user.is_authenticated():
            u = request.user
            if u.has_perm('gesualdo.validate_message'):
                comments = Message.objects.filter(piece=piece, archived=False).order_by('-timestamp')
            else:
                comments = Message.objects.filter(piece=piece, validated=True, archived=False).order_by('-timestamp') | Message.objects.filter(piece=piece, validated=False, ip=ip).order_by('-timestamp')
        else:
            comments = Message.objects.filter(piece=piece, validated=True, ip=ip, archived=False).order_by('-timestamp') | Message.objects.filter(piece=piece, validated=False, ip=ip).order_by('-timestamp')
    except Piece.DoesNotExist:
        raise Http404
    return render(request, 'main/piece.html', {'sources': sources, 'piece': piece, 'comments': comments})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def pieces(request):
    pieces = Piece.objects.all().order_by('title')
    paginator = Paginator(pieces, 25)

    page = request.GET.get('page')
    try:
        all_pieces = paginator.page(page)
    except PageNotAnInteger:
        all_pieces = paginator.page(1)
    except EmptyPage:
        all_pieces = paginator.page(paginator.num_pages)

    return render(request, 'main/pieces.html', {'pieces': all_pieces})

def texts(request):
    texts = Text.objects.all().order_by('literary_text')
    paginator = Paginator(textes, 25)

    page = request.GET.get('page')
    try:
        all_texts = paginator.page(page)
    except PageNotAnInteger:
        all_texts = paginator.page(1)
    except EmptyPage:
        all_texts = paginator.page(paginator.num_pages)

    return render(request, 'main/texts.html', {'texts': all_texts})

def texte(request, pk):
    text = Text.objects.get(slug=pk)

    return render(request, 'main/text.html', {'text':text})

def participants(request):
    return render(request, 'main/participants.html')

def lyricists(request):
    texts = Text.objects.all().distinct('author')


    return render(request, 'main/lyricists.html', {'texts': texts})



def lyricist(request, pk):
    lyrics = Piece.objects.filter(poet_lyricist=pk)

    return render(requesst,'main/lyricists.html', {'lyrics': lyrics})
