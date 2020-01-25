from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^$',business,name='business'),
    url(r'^entertainment/$',entertainment,name='entertainment'),
    url(r'^sports/$',sports,name='sports'),
    url(r'^health/$',health,name='health'),
    url(r'^science/$',science,name='science'),
    url(r'^technology/$',technology,name='technology'),

]