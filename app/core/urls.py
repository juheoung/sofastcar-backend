from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_nested import routers

from cars.views import CarViewSet, PhotoBeforeUseViewSet
from carzones.views import CarZoneViewSet
from members.views import MembersViewSet, ProfileViewSet, PhoneAuthViewSet

router = SimpleRouter(trailing_slash=False)
router.register('members', MembersViewSet)
router.register('profile', ProfileViewSet)
router.register('carzones', CarZoneViewSet)
router.register('phone_auth', PhoneAuthViewSet)
router.register('photos', PhotoBeforeUseViewSet)

"""
carzones/123/cars
"""
carzone_router = routers.NestedSimpleRouter(router, 'carzones', lookup='carzone')
carzone_router.register('cars', CarViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^', include(carzone_router.urls)),
    url(r'^api-jwt-auth/$', obtain_jwt_token),  # JWT 토큰 생성
    url(r'^api-jwt-auth/refresh/$', refresh_jwt_token),  # JWT 토큰 갱신
    url(r'^api-jwt-auth/verify/$', verify_jwt_token),  # JWT 토큰 확인
]
