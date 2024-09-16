from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addforrent', views.addForRent, name='addForRent'),
    path('deleteforrent/<int:rent_id>', views.deleteForRent, name='deleteForRent'),
    path('forsale', views.forSale, name='forSale'),
    path('addforsale', views.addForSale, name='addForSale'),
    path('deleteforsale/<int:sale_id>', views.deleteForSale, name='deleteForSale'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),
]