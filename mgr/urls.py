from django.urls import path
from mgr import sign

urlpatterns = [

    path('signin/', sign.signin),
    path('signout/', sign.signout),

]