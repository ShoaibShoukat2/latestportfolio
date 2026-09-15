from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import admin_api, views

router = DefaultRouter()
router.register(r"admin/projects", admin_api.AdminProjectViewSet, basename="admin-projects")
router.register(r"admin/skills", admin_api.AdminSkillViewSet, basename="admin-skills")
router.register(r"admin/experience", admin_api.AdminExperienceViewSet, basename="admin-experience")
router.register(r"admin/education", admin_api.AdminEducationViewSet, basename="admin-education")
router.register(r"admin/messages", admin_api.AdminMessageViewSet, basename="admin-messages")

urlpatterns = [
    path("portfolio/", views.PortfolioBundleView.as_view(), name="portfolio-bundle"),
    path("profile/", views.ProfileDetailView.as_view(), name="profile"),
    path("skills/", views.SkillListView.as_view(), name="skills"),
    path("experience/", views.ExperienceListView.as_view(), name="experience"),
    path("projects/", views.ProjectListView.as_view(), name="projects"),
    path("projects/<slug:slug>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("education/", views.EducationListView.as_view(), name="education"),
    path("contact/", views.ContactCreateView.as_view(), name="contact"),
    path("admin/login/", admin_api.AdminLoginView.as_view(), name="admin-login"),
    path("admin/logout/", admin_api.AdminLogoutView.as_view(), name="admin-logout"),
    path("admin/me/", admin_api.AdminMeView.as_view(), name="admin-me"),
    path("admin/upload/", admin_api.AdminUploadView.as_view(), name="admin-upload"),
    path("admin/profile/", admin_api.AdminProfileView.as_view(), name="admin-profile"),
    path("", include(router.urls)),
]
