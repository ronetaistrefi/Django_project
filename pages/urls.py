from django.urls import path 
from.views import PersonalPageView
from.views import EducationPageView

urlpatterns = [
    path('', PersonalPageView.as_view(), name ='personal'),
    path('education/', EducationPageView.as_view(), name ='education'),
] 