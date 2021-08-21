from django.urls import path,include
from . import views


urlpatterns = [

    path('add/',views.addpatient,name='addpatient'),
    path('viewall/',views.viewall_patient,name='viewall_patient'),
    path('view/<patient_code>',views.patient_details,name='patient_details'),
    path('',views.addpage,name='addpage'),

]