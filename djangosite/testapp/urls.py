from django.urls import path
from testapp import views

app_name = "testapp"
urlpatterns = [
    path("testapp/", views.testapp, name = 'testapp')
]
