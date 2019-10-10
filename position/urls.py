from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import JobPositionList, JobPositionDetail, JobPositionAuthentication

from position import views

urlpatterns = [
    path('', views.positions),
    path('job_list', JobPositionList.as_view()),
    path('job_list/<job_id>/', JobPositionDetail.as_view()),
    path('auth/', JobPositionAuthentication.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)


"""
url(r'^api/users_list/$', UserList.as_view(), name='user_list'),
url(r'^api/users_list/(?P<job_seeker_id>\d+)/$', UserDetail.as_view(), name='user_list'),
url(r'^api/auth/$', UserAuthentication.as_view(), name='UserAuthenticationAPI'),
"""