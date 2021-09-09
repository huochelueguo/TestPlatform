from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from background.models import DB_Book
from django.http import JsonResponse
import json
from django.contrib.postgres import serializers
from django.core import serializers

# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        # book = DB_Book(book_name=request.GET.get('book_name'))
        # book.save()
        book_name = request.GET['book_name']
        DB_Book.objects.create(book_name=book_name)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = '请输入要添加书籍名称'
        response['error_num'] = 666
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = DB_Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)