# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalInfoViewSet, SkillViewSet, ProjectViewSet, contact_view, ExperienceViewSet, EducationViewSet

router = DefaultRouter()
router.register(r'personal-info', PersonalInfoViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'education', EducationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', contact_view, name='contact'),
]