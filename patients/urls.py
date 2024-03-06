
from django.urls import path
from . import views

urlpatterns = [
        path('patient/', views.patient, name = 'patient'),
        #path('login/', views.login_user, name = 'login'),
        # path('logout/', views.logout_user, name = 'logout'),
        # path('register/', views.register_user, name = 'register'),
        path('patient_record/<int:pk>', views.patient_record, name = 'patient_record'),
        path('delete_patient/<int:pk>', views.delete_patient, name = 'delete_patient'),
        path('add_patient/', views.add_patient, name = 'add_patient'),
        path('update_patient/<int:pk>', views.update_patient, name = 'update_patient'),
        path('patient_list/', views.patient_list, name='patient_list'),
]