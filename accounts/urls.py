from django.urls import path
from .views import StudentRegistrationView
from .views import StudentLoginView
from .views import StudentProfileView


urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='student-register'),
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('student-profile/', StudentProfileView.as_view(), name='student-profile'),


]