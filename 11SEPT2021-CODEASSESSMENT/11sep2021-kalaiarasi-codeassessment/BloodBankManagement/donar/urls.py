from django.urls import path,include
from . import views


urlpatterns = [
    
    path('adding/',views.addata,name='addata'),
    path('viewscreen/',views.viewall,name='viewall'),
    #
    path('updatescreen/',views.updation,name='updatation'),
   
    

#api
    path('add/',views.adddonar,name='adddonar'),
    path('viewall/',views.donar_list,name='donar_list'),
    path('viewone/<id>',views.donar_details,name='donar_details'),

    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
    path('updateaction/',views.updatedataread,name='updatedataread'),
    
    path('loginscreen/',views.loginn,name='loginn'),
    path('welcomescreen/',views.welcomee,name='welcomee'),
    
    path('logincheck/',views.login_check,name='login_check'),
    


]
