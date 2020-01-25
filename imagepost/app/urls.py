from django.conf.urls import url
from .views import post_view,feed_view
urlpatterns=[
    url(r'^$',feed_view),
    url(r'^post/$',post_view),

]