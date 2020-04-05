from django.urls import path,include
from rest_framework import routers
from . import views
'''
router = routers.DefaultRouter()
router.register(r'members', views.MemberViewSet)
router.register(r'activities', views.ActivityPeriodViewSet)
'''
users = views.UserViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    #path('',include(router.urls)),
    path('',users,name='users'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
