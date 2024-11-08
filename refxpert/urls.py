from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("user/", views.userPage, name="user"),


    path("account/", views.account, name="account"),
    path("user/utility/", views.utility, name="utility"),
    path("legalservices/", views.legalservices, name="legalservices"),
    path("legalservices_view/<int:pk>/", views.legalservices_view, name="legalservices_view"),
    path("propertymanagement/", views.propertymanagement, name="propertymanagement"),
    path("propertymanagement_view/<int:pk>/", views.propertymanagement_view, name="propertymanagement_view"),


    path("tenantref/", views.tenantref, name="tenantref"),
    path('tenantform/', views.tenantform, name="tenantform"),
    path("tenantform_view/<int:pk>/", views.tenantform_view, name="tenantform_view"),
    path("ref_optionform/", views.ref_option, name="ref_optionform"),
    path("emailtenant/", views.email_tenants, name="emailtenant"),

    path("contact/", views.contact, name="contact"),
    path("careers/", views.careers, name="careers"),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('about/', TemplateView.as_view(template_name="refxpert/components/about.html"), name='about'),

    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="refxpert/password/password_reset.html"), name="reset_password"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="refxpert/password/password_reset_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="refxpert/password/password_reset_form.html"), name="password_reset_confirm"), 
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="refxpert/password/password_reset_done.html"), name="password_reset_complete"),

    path('delete_tenant/<int:pk>/', views.delete_tenant, name='delete_tenant'),
    path('delete_service/<int:pk>/', views.delete_service, name='delete_service'),
    path('delete_property/<int:pk>/', views.delete_property, name='delete_property'),

    
    path('tenancy_post_view/<int:pk>/', views.tenancy_post_view, name='tenancy_post_view'),
    path('tenancy_post/', views.tenancy_post, name='tenancy_post'),
    #path('test/', views.test_view, name='test'),

    path('legal_post/', views.legal_post, name='legal_post'),
    path('property_post/', views.property_post, name='property_post'),
   
]