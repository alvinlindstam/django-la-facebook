from django.conf.urls import patterns, url

urlpatterns = patterns('test_project.connect.views',
    url(r'^/?$', "test_index", name="index"),
    url(r'^after/?$', "after", name="after"),
)
