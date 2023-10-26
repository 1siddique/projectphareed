from django.contrib import admin
from django.urls import path,include
from .views import appTHREE_RI ,register,Aboutus,contact,signin ,course,index,signout,feedback


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',appTHREE_RI),
    path('Aboutus/', Aboutus, name="Aboutus"),
    path('SingUp/',register,name="SingUp"),
    path('signin/',signin,name="signin"),
    path('contact/',contact,name='contact'),
    path('course/',course,name='course'),
    path('index/',index,name='index'),
    path('sing Out/',signout,name="sing Out"),
    path('feedback/',feedback,name="feedback"),



]