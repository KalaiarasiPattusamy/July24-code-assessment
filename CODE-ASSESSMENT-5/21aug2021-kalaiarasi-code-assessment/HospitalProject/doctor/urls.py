from django.urls import path,include
from . import views


urlpatterns = [

    path('add/',views.adddoctor,name='adddoctor'),
    path('viewall/',views.viewall_doctor,name='viewall_doctor'),
    path('view/<doctor_code>',views.doctor_details,name='doctor_details'),
    path('register/',views.registerpage,name='registerpage'),
    path('login/',views.loginpage,name='loginpage'),

]