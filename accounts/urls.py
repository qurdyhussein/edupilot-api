from django.urls import path
from .views import StudentRegistrationView
from .views import StudentLoginView


urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='student-register'),
    path('login/', StudentLoginView.as_view(), name='student-login'),

]