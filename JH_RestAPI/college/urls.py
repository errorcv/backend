from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from college import views

urlpatterns = [
    path('', views.get_colleges),
    path('majors', views.get_majors),
    path('college_majors',
         views.college_majors),
]
urlpatterns = format_suffix_patterns(urlpatterns)
