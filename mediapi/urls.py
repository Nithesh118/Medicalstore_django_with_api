from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup,name='signup_api'),
    path('login', views.login, name='login_api'),
    path('create', views.create, name='createapi'),
    path('list', views.list, name='retrieveproductapi'),
    path('<int:pk>/update', views.update, name='updateproductapi'),
    path('<int:pk>/delete', views.delete, name='deleteproductapi'),
    path('search/<str:query>/',views.search,name='search')
]