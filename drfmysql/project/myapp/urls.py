from django.conf.urls import url
from rest_framework import routers
from project.myapp.views import StudentViewSet, UniversityViewSet, ExpenseViewSet,CustomView
 
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'expenses', ExpenseViewSet)
urlpatterns = [
    url(r'customview', CustomView.as_view()),
]
 
urlpatterns += router.urls