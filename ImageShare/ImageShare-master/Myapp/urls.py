
from django.conf.urls import url
from . views import signup_view,login_view,feed_view, post_view,like_view,comment_view,logout

urlpatterns = [
    url(r'^$',signup_view),
    url(r'^login/$',login_view),
    url(r'feed/',feed_view),
    url(r'post/',post_view),
    url(r'like/',like_view),
    url(r'comment/', comment_view),
    url(r'logout/', logout),
]
