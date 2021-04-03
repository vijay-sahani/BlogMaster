from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponse
from django.views.generic import UpdateView
from .forms import AddBlogForm, EditPostForm
from .models import BlogPost,Contact




# Create your views here.
def index(request):
    allPosts=BlogPost.objects.all()
    return render(request,'index.html',{'blogs':allPosts})


def handleBlog(request,id,slug):
    blog_content=BlogPost.objects.filter(id=id)
    blog_url=[ ]
    for item in BlogPost.objects.all().exclude(id=id):
        blog_url.append((item.title,item.id))
    return render(request,'blogPost.html',{'blogs':blog_content,'other_urls':blog_url})
   
def writeBlog(request):
    if request.method=='POST':
        try:
            if request.user.is_authenticated:
                form=AddBlogForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request,f'<strong>Blog Uploaded Successfully</strong> view your blog <a href="article/{form.instance.id}/{form.instance}">here</a>')
                else:
                    print(form.errors)
            else:
                messages.warning(request,'<strong>Sign up Required!</strong> Please Signup first to write a blog.')
        except Exception as e:
            print(e)
            messages.error(request,'<strong>An Error has Occured!</strong> Please try again. If you see the same error again please contact us.')
    form = AddBlogForm()
    return render(request, 'AddBlog.html', {'form' : form})

def showArticles(request):
    allPosts=BlogPost.objects.all()
    return render(request,'articles.html',{'blogs':allPosts})

def myPost(request):
    if request.method=='GET':
        query=request.GET['query']
        results=BlogPost.objects.filter(title_icontains=query)
        if results.count()==0:
            return None
    allpost=BlogPost.objects.filter(user=request.user)
    return render(request,'myPost.html',{'posts':allpost})

class EditPost(UpdateView):
    form_class=EditPostForm
    model=BlogPost
    template_name='update_post.html'

def deletePost(request,id):
    try:
        post_id= BlogPost.objects.get(id=id)
    except:
        messages.error(request,'<strong>Error! </strong>You are not allowed to delete other\'s article')
        return redirect('index')
    if request.user.username==post_id.user.username:
        post_id.delete()
        return redirect('mypost')
    else:
        messages.error(request,'<strong>Error! </strong>You are not allowed to delete other\'s article')
    return redirect('index')
    
def docs(request):
    messages.warning(request,'<strong>Under Progress!</strong> Currently I am working on the Docmentation, So right now you might not find this helpful')
    return render(request,'docs.html')

def contact_us(request):
    if request.method=='POST':
        name=f"{request.POST['fname']} {request.POST['lname']}"
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        feedback=Contact(name=name,email=email,phone=phone,message=message)
        feedback.save()
        messages.success(request,'<strong>Thanks for Contacting us</strong>. I will get back to soon. Till then have great day!')
        return redirect('index')
    return render(request,'404.html')


