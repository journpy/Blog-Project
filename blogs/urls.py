from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-blog/', views.create_blog, name='create-blog'),
    path('success', views.success, name='success'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog-detail'),
    path('blogs/update-blog/<int:blog_id>/', views.update_blog, name='update-blog'),
    path('blogs/delete-blog/<int:blog_id>/', views.delete_blog, name='delete-blog'),
]