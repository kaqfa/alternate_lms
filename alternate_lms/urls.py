from django.conf.urls import include, url
from django.contrib import admin

import base.views as vbase
import member.views as vmember
import course.views as vcourse

urlpatterns = [
    url(r'^login/', vmember.LoginView.as_view(), name='login'),
    url(r'^$', vbase.IndexView.as_view(), name='index'),
    url(r'^course/(?P<pk>\d+)/front', vcourse.FrontView.as_view(), name='coursefront'),
    url(r'^course/(?P<pk>\d+)/outline', vcourse.OutlineView.as_view(), name='courseoutline'),
    url(r'^course/(?P<pk>\d+)/grades', vcourse.GradeView.as_view(), name='coursegrade'),
    url(r'^admin/', include(admin.site.urls)),
]