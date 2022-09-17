from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('update_recipe/<slug:slug>', views.update_recipe, name='update_recipe'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]