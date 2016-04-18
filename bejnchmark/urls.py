from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^templatetags/([0-9]+)/([0-9]+)', views.templatetags),
    url(r'^includes/([0-9]+)/([0-9]+)', views.includes),
]
