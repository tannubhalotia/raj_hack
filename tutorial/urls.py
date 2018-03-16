from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views

urlpatterns = [
    url(r'^tableadmin/', admin.site.urls),
    url(r'^table1/$',views.Table1View.as_view()),
    url(r'^table2/$',views.Table2View.as_view()),
    url(r'^table3/$',views.Table3View.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

