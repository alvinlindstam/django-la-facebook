from django.conf.urls.defaults import *


urlpatterns = patterns("la_facebook.views",
    url(r"^login/?$", "facebook_login", name="la_facebook_login"),
    url(r"^callback/?$", "facebook_callback", name="la_facebook_callback"),
)
