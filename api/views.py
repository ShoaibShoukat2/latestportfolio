from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile, Skill, Experience, Project, Education, ContactMessage
from .serializers import (
    ProfileSerializer,
    SkillSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    EducationSerializer,
    ContactMessageSerializer,
)


class PortfolioBundleView(APIView):
    """Single endpoint that returns the full public portfolio payload."""

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        profile = Profile.objects.first()
        return Response(
            {
                "profile": ProfileSerializer(profile).data if profile else None,
                "skills": SkillSerializer(Skill.objects.all(), many=True).data,
                "experience": ExperienceSerializer(Experience.objects.all(), many=True).data,
                "projects": ProjectSerializer(Project.objects.all(), many=True).data,
                "education": EducationSerializer(Education.objects.all(), many=True).data,
            }
        )


class ProfileDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.first()


class SkillListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ExperienceListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ProjectListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"


class EducationListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ContactCreateView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"ok": True, "message": "Thanks — your message is on my desk."},
            status=status.HTTP_201_CREATED,
        )
