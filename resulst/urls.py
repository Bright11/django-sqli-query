from django.urls import path

from . import views

app_name="resulst"
urlpatterns = [
    path("",views.index.as_view(),name="index"),
    path('pullingresult',views.pullingresult.as_view(),name="pullingresult"),

    path("newresults",views.newresults.as_view(),name="newresults")
]
