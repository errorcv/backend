from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import CompanyList, CompanyDetail, CompanyAuthentication

from company import views

urlpatterns = [
    path('', views.companies),
    path('add/', CompanyList.as_view()),
    path('<int:company_id>/', CompanyDetail.as_view()),
    path('auth/', CompanyAuthentication.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
