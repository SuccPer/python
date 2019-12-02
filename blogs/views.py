from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from   django.http import  HttpResponse
from  blogs.models import  *
from datetime import datetime
from django.http import Http404

#create your views here.

def home1(request):
    return HttpResponse("Hello World,Django")

def hello(request):
    es = Person.objects.get(name='小明')
    name = es.name
    age = es.age
    return HttpResponse(name)

# def  hello_0(request):
#     p = Person(name="张三")
#     p.age = 15
#     p.save()
#     return  HttpResponse("增加数据库")

def  hello_1(request):
    p = Person(name="李四")
    p.age = 25
    p.save()
    return  HttpResponse("增加一条新的表格记录")

# def  hello_3(request):
#     p = Person(name="李六")
#     p.age = 23
#     p.save()
#     return  HttpResponse("增加一条李六的信息")

def home(request):
    return  render(request,'home.html')
    # return render_to_response('home.html')

def base(request):
    return  render(request,'base.html')
    # return render_to_response('home.html')

def test(request):
    string = u"Shiyanlou is very good!"
    return render(request,'test.html',{'string':string})

def test2(request):
    TutorialList = ["HTML","CSS","JQUEERY","Python","Django"]
    return render(request,'test2.html',{'TutorialList':TutorialList})

def userinfo(request):
    name = 'xiaoming'
    age = 25
    return render(request,'userinfo.html',locals())

def  add(request):
    Articles.objects.create(title="hello world",lab='python',content='Let us add a database item')
    Articles.objects.create(title="Django",lab='python',content='It is a django_test')
    Articles.objects.create(title="早上好",lab='问好',content='今天天气很好')
    Articles.objects.create(title="半期考试通知",lab='通知',content='5月12日半期考')
    return HttpResponse("增加Articles数据")

def select(request):
    # a = Articles.objects.all()
    a = Articles.objects.filter(title="hello world")
    for i in a:
        lab = i.lab
        content = i.content
        date = i.date_time
        print(lab)
    return render(request, 'get.html', {'lab': lab, 'content': content, 'date':date})
    # all = Articles.objects.filter(title="hello world")
    # for i in a:
    #     lab = i.lab
    #     content = i.content
    # return render(request,'get.html',{'lab' :lab,'content' : content})
    # return render(request, 'get.html', {'all':all})
    # return render(request, 'get.html', {'b':a})

def home(request):
    # return HttpResponse("hello everyone")
    post_list =Articles.objects.all()
    return render(request,'home.html',{'post_list':post_list})

# def detail(request,my_args):
    # post = Articles.objects.all()[int(my_args)]
    # str = ("title = %s , lab = %s , date_time = %s,content=%s"
    #        %(post.title,post.lab,post.date_time,post.content))
    # return  HttpResponse(str)
        #return HttpResponse("You are looking at my_args %s" %my_args)

def test(request):
    return render(request,'test3.html',{'current_time':datetime.now()})

def detail(request,id):
    try:
        post = Articles.objects.get(id=str(id))
    except Articles.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})