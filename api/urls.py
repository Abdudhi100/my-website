from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationViewSet, CertificateViewSet, ExperienceViewSet, SkillViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'education', EducationViewSet, basename='education')
router.register(r'certificates', CertificateViewSet, basename='certificates')
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'skills', SkillViewSet, basename='skills')
router.register(r'contacts', ContactViewSet, basename='contacts')

urlpatterns = [
    path('api/', include(router.urls)),
]