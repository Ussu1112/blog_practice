from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogPost
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects #쿼리셋 #메소드
    blog_list=Blog.objects.all()#블로그 모든 글들을 대상으로
    paginator = Paginator(blog_list,3) #블로그 객체 새 개를 한페이지로 자르기
    page = request.GET.get('page') #request된 페이지가 뭔지를 알아내고
    posts = paginator.get_page(page) #request된 페이지를 얻어온 뒤 리턴 해준다.

    return render(request, 'home.html', {'blogs': blogs,'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_data = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})