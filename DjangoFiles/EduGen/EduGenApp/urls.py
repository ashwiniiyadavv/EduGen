from django.urls import path
from .views import ReactAppView, index,feedback
urlpatterns=[
    #path('', ReactAppView.as_view(), name='react-app')
    path('', index, name='index'),
    path('/generate_video',index,name='generate_video'),
    path("/feedback",feedback, name="submit_feedback")
    
]