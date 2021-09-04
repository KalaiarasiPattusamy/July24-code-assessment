from django.urls import path,include
from . import views


urlpatterns = [
    
    path('adding/',views.addata,name='addata'),
    path('viewallscreen/',views.viewall,name='viewall'),
    path('searchscreen/',views.searchcode,name='searchcode'),
    path('updatescreen/',views.updation,name='updatation'),
    path('deletescreen/',views.deletion,name='deletion'),
    path('welcomefaculty/',views.facultyPage,name='facultyPage'),
    path('login/', views.loginview, name='loginview'),
#api
    path('add/',views.addfaculty,name='addfaculty'),
    path('viewall/',views.faculty_list,name='faculty_list'),
    path('viewone/<id>',views.faculty_details,name='faculty_details'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
    path('updateaction/',views.updatedataread,name='updatedataread'),
    path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteaction/',views.deletedataread,name='deletedataread'),
    path('loginAction/', views.login_check, name='login_check'),
    path('viewprofile/', views.prof_view, name='prof_view'),
]
