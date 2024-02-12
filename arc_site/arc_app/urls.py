from django.urls import path
from . import views
from .views import contact_view
from .views import blog


urlpatterns = [
    path('', views.home, name='home2'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('posts/', blog, name='blog_posts_view'),
    path('blog/<int:post_id>/', views.post_detail, name='post_detail'),
    path('aboutex/', views.aboutex, name='aboutex'),
    path('contact/', contact_view, name='contact_view')

]