from django.utils.text import slugify
from rest_framework import serializers
from .models import Profile, Skill, Experience, Project, Education, ContactMessage


def coerce_list(value):
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        parts = value.split("\n") if "\n" in value else value.split(",")
        return [part.strip() for part in parts if part.strip()]
    return value


def normalize_url(value):
    value = (value or "").strip()
    if not value:
        return ""
    if not value.startswith(("http://", "https://")):
        return f"https://{value}"
    return value


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"

    def validate_highlights(self, value):
        return coerce_list(value)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        extra_kwargs = {
            "live_url": {"allow_blank": True, "required": False},
            "repo_url": {"allow_blank": True, "required": False},
            "image_url": {"allow_blank": True, "required": False},
            "slug": {"required": False, "allow_blank": True},
        }

    def validate_stack(self, value):
        return coerce_list(value)

    def validate_features(self, value):
        return coerce_list(value)

    def validate_live_url(self, value):
        return normalize_url(value)

    def validate_repo_url(self, value):
        return normalize_url(value)

    def validate_slug(self, value):
        return slugify(value) if value else value

    def create(self, validated_data):
        if not validated_data.get("slug"):
            validated_data["slug"] = self._unique_slug(validated_data.get("title", "project"))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "slug" in validated_data and not validated_data["slug"]:
            validated_data["slug"] = self._unique_slug(
                validated_data.get("title", instance.title),
                exclude_id=instance.id,
            )
        return super().update(instance, validated_data)

    def _unique_slug(self, title, exclude_id=None):
        base = slugify(title) or "project"
        slug = base
        index = 2
        qs = Project.objects.all()
        if exclude_id:
            qs = qs.exclude(pk=exclude_id)
        while qs.filter(slug=slug).exists():
            slug = f"{base}-{index}"
            index += 1
        return slug


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["id", "name", "email", "subject", "message", "created_at"]
        read_only_fields = ["id", "created_at"]


class ContactMessageAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        read_only_fields = ["id", "created_at", "name", "email", "subject", "message"]
