from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=120, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)
    years_experience = models.PositiveIntegerField(default=0)
    projects_delivered = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("database", "Database"),
        ("devops", "DevOps"),
        ("tools", "Tools"),
    ]

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.PositiveIntegerField(default=80, help_text="0-100 proficiency")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return f"{self.name} ({self.category})"


class Experience(models.Model):
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.CharField(max_length=40)
    end_date = models.CharField(max_length=40, default="Present")
    description = models.TextField()
    highlights = models.JSONField(default=list, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("medical", "Medical"),
        ("travel", "Travel"),
        ("booking", "Booking"),
        ("ai", "AI Agents"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")
    stack = models.JSONField(default=list, blank=True)
    features = models.JSONField(default=list, blank=True)
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    image_url = models.CharField(max_length=500, blank=True)
    accent = models.CharField(max_length=20, default="#0F766E")
    featured = models.BooleanField(default=True)
    year = models.CharField(max_length=10, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200, blank=True)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    details = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]
        verbose_name_plural = "education"

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.subject}"
