from django.conf.urls import url

from . import views

app_name = 'log_viewer'

urlpatterns = [
    url(r'^(?P<file_name>[\.\w-]*)/(?P<page>[0-9]+)', views.log_viewer,
        name='logfile-view'),
    url(r'^(?P<file_name>[\.\w-]*)', views.log_viewer,
        name='logfile-view'),

]
