from django.urls import path
from . import views

# This Section is called URL Mapping

urlpatterns = [
    # name property is using for linking navbar url- call this name in link href section
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("booking/", views.booking, name='booking'),
    path("doctors/", views.doctors, name='doctors'),
    path("department/", views.department, name='department'),
    path("contact/", views.contact, name='contact'),
    path("signup/", views.signup, name='signup'),
    path("signin/", views.signin, name='signin'),
    path("logout/", views.logout, name='logout'),
]