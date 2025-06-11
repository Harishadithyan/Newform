from django.urls import path
from .views import submit_feedback

urlpatterns = [
    path('api/feedback/', submit_feedback),
]