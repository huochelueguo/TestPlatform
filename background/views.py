from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from background.models import DB_Book
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.postgres import serializers
from django.core import serializers
from django.contrib import auth
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

def login_action(request):
    u_name = request.GET['username']
    p_pwd = request.GET['password']
    print(u_name, p_pwd)
    user = auth.authenticate(username=u_name, password=p_pwd)
    if user is not None:
        # return redirect('/homepage/')
        auth.login(request, user)
        request.session['user'] = u_name
        return HttpResponse("成功")
    else:
        return HttpResponse('用户名或密码错误，登录失败')