from app import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('articles/<slug:slug>/', views.ArticleDetailView, name='article-detail'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
]
