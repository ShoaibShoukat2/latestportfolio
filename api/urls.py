from django.urls import path
from . import views

urlpatterns = [
    path("portfolio/", views.PortfolioBundleView.as_view(), name="portfolio-bundle"),
    path("profile/", views.ProfileDetailView.as_view(), name="profile"),
    path("skills/", views.SkillListView.as_view(), name="skills"),
    path("experience/", views.ExperienceListView.as_view(), name="experience"),
    path("projects/", views.ProjectListView.as_view(), name="projects"),
    path("projects/<slug:slug>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("education/", views.EducationListView.as_view(), name="education"),
    path("contact/", views.ContactCreateView.as_view(), name="contact"),
]
