from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import JobPositionList, JobPositionDetail, JobPositionAuthentication

from position import views

urlpatterns = [
    path('', views.positions),
    path('add/', JobPositionList.as_view()),
    path('<int:job_id>/', JobPositionDetail.as_view()),
    path('auth/', JobPositionAuthentication.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
