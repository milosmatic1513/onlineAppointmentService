from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('register/',views.register_view,name="register"),
    path('logout/',views.logoutUser,name="logout")

]
