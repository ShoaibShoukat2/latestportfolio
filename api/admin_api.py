from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.contrib.auth import authenticate
from django.core.files.storage import default_storage
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ContactMessage, Education, Experience, Profile, Project, Skill
from .serializers import (
    ContactMessageAdminSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProfileSerializer,
    ProjectSerializer,
    SkillSerializer,
)

ALLOWED_IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}


class AdminLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = (request.data.get("username") or "").strip()
        password = request.data.get("password") or ""
        user = authenticate(request, username=username, password=password)
        if not user or not user.is_active or not user.is_staff:
            return Response(
                {"detail": "Invalid username or password."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})


class AdminLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({"ok": True})


class AdminMeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        unread = ContactMessage.objects.filter(is_read=False).count()
        return Response(
            {
                "username": request.user.username,
                "counts": {
                    "projects": Project.objects.count(),
                    "skills": Skill.objects.count(),
                    "experience": Experience.objects.count(),
                    "education": Education.objects.count(),
                    "messages": ContactMessage.objects.count(),
                    "unread": unread,
                },
            }
        )


class AdminUploadView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        uploaded = request.FILES.get("file")
        if not uploaded:
            return Response({"detail": "Choose an image file."}, status=status.HTTP_400_BAD_REQUEST)
        ext = Path(uploaded.name).suffix.lower()
        if ext not in ALLOWED_IMAGE_EXTS:
            return Response(
                {"detail": "Use a PNG, JPG, WEBP, GIF, or SVG image."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        filename = f"projects/{uuid4().hex}{ext}"
        saved = default_storage.save(filename, uploaded)
        relative = f"{settings.MEDIA_URL}{saved}".replace("//", "/")
        absolute = request.build_absolute_uri(relative)
        return Response({"url": absolute, "path": relative})


class AdminProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_object(self):
        return Profile.objects.first()

    def get(self, request):
        profile = self.get_object()
        if not profile:
            return Response({})
        return Response(ProfileSerializer(profile).data)

    def put(self, request):
        return self._save(request, partial=False)

    def patch(self, request):
        return self._save(request, partial=True)

    def _save(self, request, partial):
        profile = self.get_object()
        serializer = ProfileSerializer(profile, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AdminProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class AdminSkillViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class AdminExperienceViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class AdminEducationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class AdminMessageViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageAdminSerializer
    http_method_names = ["get", "patch", "delete", "head", "options"]
