"""urlproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from adminapp import views as adminapp_views
from userapp import views as userapp_views
from mainapp import views as mainapp_views

urlpatterns = [
    #adminapp
    path('admin/', admin.site.urls),
    path('admin-index',adminapp_views.admin_index,name='admin_index'),
    path('admin-add-data',adminapp_views.admin_add_data,name='admin_add_data'),
    path('admin-run-algorithm/<int:data>',adminapp_views.admin_run_algorithm,name='admin_run_algorithm'),
    path('admin-score/<int:id>/',adminapp_views.admin_score,name='admin_score'),
    path('LogisticRegression/<int:id>',adminapp_views.LogisticRegression,name='LogisticRegression'),
    path('SVM/<int:id>',adminapp_views.SVM,name='SVM'),
    path('KNeighborsRegressor/<int:id>',adminapp_views.KNeighborsRegressor,name='KNeighborsRegressor'),
    path('LSTM/<int:id>',adminapp_views.LSTM,name='LSTM'),
    path('RandomForest/<int:id>',adminapp_views.RandomForest,name='RandomForest'),
    path('admin-graphanalysis',adminapp_views.admin_graph_analysis,name='admin_graph_analysis'),
    path('pending_users',adminapp_views.pending_users,name='pending_users'),
    path('all_users',adminapp_views.all_users,name='all_users'),
    path('accept-user/<int:id>', adminapp_views.accept_user, name = 'accept_user'),
    path('reject-user/<int:id>', adminapp_views.reject_user, name = 'reject'),
    path('delete-user/<int:id>', adminapp_views.delete_user, name = 'delete_user'),
    path('delete-dataset/<int:id>', adminapp_views.delete_dataset, name = 'delete_dataset'),
    # path('predict/<int:id>',adminapp_views.predict,name='predict'),
    #mainapp
    path('',mainapp_views.main_index,name='main_index'),
    path('main-about',mainapp_views.main_about,name='main_about'),
    path('main-admin-login',mainapp_views.main_admin_login,name='main_admin_login'),
    path('main-user-login',mainapp_views.main_user_login,name='main_user_login'),
    path('main-user-registration',mainapp_views.main_user_registration,name='main_user_registration'),
    path('main_contact',mainapp_views.main_contact,name='main_contact'),
    path('main_otp',mainapp_views.main_otp,name='main_otp'),
    #userapp
    path('user-index',userapp_views.user_index,name='user_index'),
    path('user-myprofile',userapp_views.user_myprofile,name='user_myprofile'),
    path('user-url',userapp_views.user_url,name='user_url'),
    path('user-scan',userapp_views.user_scan, name='user_scan'),

]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
