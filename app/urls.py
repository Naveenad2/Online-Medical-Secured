from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main_page,name='main_page'),
   
    path('doctor_r',views.doctor_registration,name='doctor_r'),
    path('doctor_r_auth',views.doctor_r_auth,name='doctor_r_auth'),


    path('patient_r',views.patient_reg,name='doctor_r'),
    path('patient_r_auth',views.patient_r_auth,name='patient_r_auth'),

    path('patient_login',views.patient_login,name='patient_l'),
    path('doctor_login',views.doctor_login,name='doctor_login'),

    path('Slogin',views.Slogin,name='Slogin'),
    path('Sregistration',views.Sregistration,name='Sregistration'),

    path('patientMainPage',views.patientMainPage,name='patientMainPage'),
    path('doctorMainPage',views.doctorMainPage,name='doctorMainPage'),

     path('viewAllDoctors',views.viewAllDoctors,name='viewAllDoctors'),
      path('doctorCosult/<int:id>',views.doctorCosult,name='doctorCosult'),

      path('doctorCosult/<int:id>',views.doctorCosult,name='doctorCosult'),
      path('cosultation_imp',views.cosultation_imp,name='cosultation_imp'),
       path('addTimmingDoctor/<int:id>',views.addTimmingDoctor,name='addTimmingDoctor'),
        path('addTimmingDoctorImplementation',views.addTimmingDoctorImplementation,name='addTimmingDoctorImplementation'),
         path('editPatient',views.editPatient,name='editPatient'),
          path('editDoctor',views.editDoctor,name='editDoctor'),




    path('logout',views.Logout_,name='logout'),

   
]



