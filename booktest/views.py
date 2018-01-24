#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader


# Create your views here.
def index(request):
     return HttpResponse('Hello World!')

def detail(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))

#页面
def getTest1(request):
    t = loader.get_template('booktest/getTest1.html')
    context = RequestContext(request,{'h1':'hello'})
    return  HttpResponse(t.render(context))
    # return render(request,'booktest/getTest1.html')

#接收一键一值的情况
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/getTest2.html',context)

#一键多值的情况
def getTest3(request):
    a = request.GET.getlist('a')
    context = {'a':a}
    return render(request,'booktest/getTest3.html',context)

def postTets1(request):
    return render(request,'booktest/postTest1.html')

def postTets2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,
               'upwd':upwd,
               'ugender':ugender,
               'uhobby':uhobby,
               }
    return render(request,'booktest/postTest2.html',context)

def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])
    else:
        response.set_cookie('t1','abc')
    return response

def redTest1(request):
    # return HttpResponseRedirect('/booktest/redTest2/')
    return redirect('/booktest/redTest2/')

def redTest2(request):
    return HttpResponse('这是转向来的页面！')