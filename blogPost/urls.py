from django.urls import path
from .views import EditPost
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('article/<int:id>/<str:slug>',views.handleBlog,name='detailView'),
    path('add-post',views.writeBlog,name='addBlog'),
    path('my-post',views.myPost,name='mypost'),
    path('edit/article/<int:pk>',EditPost.as_view()),
    path('delete/post/<int:id>',views.deletePost),
    path('docs',views.docs),
    path('contact',views.contact_us),
]