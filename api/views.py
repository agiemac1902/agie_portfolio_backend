# api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from .models import PersonalInfo, Skill, Project, Contact, Experience, Education
from .serializers import PersonalInfoSerializer, SkillSerializer, ProjectSerializer, ContactSerializer, ExperienceSerializer, EducationSerializer

class PersonalInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

@api_view(['POST'])
def contact_view(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        # Send email
        send_mail(
            subject=f"Portfolio Contact: {serializer.validated_data['subject']}",
            message=f"Name: {serializer.validated_data['name']}\nEmail: {serializer.validated_data['email']}\n\nMessage:\n{serializer.validated_data['message']}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["machiyagrippa@gmail.com"],
            fail_silently=False,
        )
        
        return Response({"message": "Message sent successfully"})
    return Response(serializer.errors, status=400)