from django.urls import path,include
from medicines import views


urlpatterns = [
    path('',views.home,name='home'),
    path('list/', views.list_medicines, name='list_medicines'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_medicine, name='add_medicine'),
    path('edit/<int:medicine_id>/', views.edit_medicine, name='edit_medicine'),
    path('delete/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),
    path('search/', views.search_medicine, name='search_medicine'),
    path('mediapi/', include('mediapi.urls')),
    
]


