from django.core.management.base import BaseCommand
from api.models import Profile, Skill, Experience, Project, Education


class Command(BaseCommand):
    help = "Seed portfolio content for Shoaib Shoukatha"

    def handle(self, *args, **options):
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Education.objects.all().delete()

        Profile.objects.create(
            name="Shoaib Shoukatha",
            title="Full Stack Developer",
            tagline="I ship medical platforms, travel apps, booking systems, and AI agents — end to end.",
            about=(
                "I am a Full Stack Developer who builds real products people use daily: "
                "live doctor–patient consulting apps, boat booking platforms like Smagua Travels, "
                "agency sites for tickets and hotels, and AI agent systems with practical workflows. "
                "I work across React frontends and Django backends — from API design and databases "
                "to polished, responsive interfaces that feel professional in production."
            ),
            email="hello@shoaib.dev",
            phone="+923001234567",
            location="Pakistan · Remote Worldwide",
            github="https://github.com",
            linkedin="https://www.linkedin.com/in/",
            twitter="https://x.com",
            resume_url="#",
            years_experience=5,
            projects_delivered=40,
        )

        skills = [
            ("React", "frontend", 92, 1),
            ("TypeScript", "frontend", 88, 2),
            ("Next.js", "frontend", 84, 3),
            ("Vite", "frontend", 90, 4),
            ("Mobile UI", "frontend", 86, 5),
            ("Python", "backend", 93, 1),
            ("Django", "backend", 91, 2),
            ("DRF", "backend", 90, 3),
            ("WebRTC / Live", "backend", 84, 4),
            ("REST / GraphQL", "backend", 88, 5),
            ("PostgreSQL", "database", 87, 1),
            ("MySQL", "database", 80, 2),
            ("Redis", "database", 78, 3),
            ("Docker", "devops", 85, 1),
            ("CI/CD", "devops", 80, 2),
            ("AWS / Nginx", "devops", 76, 3),
            ("Git", "tools", 94, 1),
            ("Figma", "tools", 75, 2),
            ("Postman", "tools", 88, 3),
        ]
        Skill.objects.bulk_create(
            [Skill(name=n, category=c, level=l, order=o) for n, c, l, o in skills]
        )

        Experience.objects.bulk_create(
            [
                Experience(
                    company="Product & Client Builds",
                    role="Senior Full Stack Developer",
                    location="Remote",
                    start_date="2023",
                    end_date="Present",
                    description=(
                        "Leading delivery of telehealth, travel booking, and AI-assisted "
                        "product experiences with React frontends and Django APIs."
                    ),
                    highlights=[
                        "Shipped live doctor–patient video consulting flows",
                        "Built boat booking + listing apps for travel brands",
                        "Integrated ticket/hotel reservation systems for agencies",
                    ],
                    order=1,
                ),
                Experience(
                    company="Cascade Labs",
                    role="Full Stack Engineer",
                    location="Lahore",
                    start_date="2021",
                    end_date="2023",
                    description=(
                        "Built customer portals, payment integrations, and admin tooling "
                        "for logistics and consumer apps."
                    ),
                    highlights=[
                        "Delivered 12 client products from discovery to launch",
                        "Introduced automated test suites and staging pipelines",
                        "Owned PostgreSQL schema migrations at scale",
                    ],
                    order=2,
                ),
                Experience(
                    company="Freelance / Studio Work",
                    role="Full Stack Developer",
                    location="Worldwide",
                    start_date="2019",
                    end_date="2021",
                    description=(
                        "Partnered with founders to ship MVPs — mobile-ready web apps, "
                        "dashboards, and booking platforms with Django + React."
                    ),
                    highlights=[
                        "Launched 15+ MVPs under tight timelines",
                        "Handled hosting, domains, and handoff docs",
                    ],
                    order=3,
                ),
            ]
        )

        Project.objects.bulk_create(
            [
                Project(
                    title="MediLink Live Consult",
                    slug="medilink-live-consult",
                    category="medical",
                    summary="Live patient–doctor video consulting for online medical care.",
                    description=(
                        "A medical platform where patients book appointments and join "
                        "secure live video calls with doctors for online consultations. "
                        "Includes doctor availability, patient records, prescriptions, "
                        "and realtime call status — built for clinics that want telehealth "
                        "without sacrificing trust or UX."
                    ),
                    stack=["React", "Django", "WebRTC", "DRF", "PostgreSQL", "Redis"],
                    features=[
                        "Live doctor–patient video calls",
                        "Appointment scheduling",
                        "Secure patient records",
                        "Prescription & notes after consult",
                    ],
                    live_url="https://example.com",
                    repo_url="https://github.com",
                    image_url="/images/projects/medilink-live-consult.png",
                    accent="#0E7490",
                    featured=True,
                    year="2025",
                    order=1,
                ),
                Project(
                    title="Smagua Travels",
                    slug="smagua-travels",
                    category="travel",
                    summary="Mobile app for online boat booking and listing management.",
                    description=(
                        "Smagua Travels is a travel mobile experience where users browse "
                        "boat listings, check availability, and book trips online. Operators "
                        "can publish boats, manage schedules, and track bookings — a clean "
                        "marketplace flow from discovery to confirmed reservation."
                    ),
                    stack=["React Native", "React", "Django", "DRF", "PostgreSQL", "Maps"],
                    features=[
                        "Online boat booking",
                        "Boat listing & gallery",
                        "Availability calendar",
                        "Operator dashboard",
                    ],
                    live_url="https://example.com",
                    repo_url="https://github.com",
                    image_url="/images/projects/smagua-travels.png",
                    accent="#0369A1",
                    featured=True,
                    year="2025",
                    order=2,
                ),
                Project(
                    title="Voyage Agency Desk",
                    slug="voyage-agency-desk",
                    category="booking",
                    summary="Agency website for flight tickets and hotel reservations.",
                    description=(
                        "A full agency web platform for searching and booking flight tickets "
                        "plus hotel reservations in one place. Customers compare options, "
                        "hold bookings, and pay securely; agents manage inventory, "
                        "confirmations, and customer requests from an admin console."
                    ),
                    stack=["React", "Django", "DRF", "PostgreSQL", "Payments", "Nginx"],
                    features=[
                        "Ticket search & booking",
                        "Hotel reservation flow",
                        "Agent admin panel",
                        "Payment & confirmation emails",
                    ],
                    live_url="https://example.com",
                    repo_url="https://github.com",
                    image_url="/images/projects/voyage-agency-desk.png",
                    accent="#B45309",
                    featured=True,
                    year="2024",
                    order=3,
                ),
                Project(
                    title="Aether AI Agents",
                    slug="aether-ai-agents",
                    category="ai",
                    summary="Multi-agent AI workspace that automates research, support, and ops tasks.",
                    description=(
                        "A visual AI agents platform where specialized agents handle research, "
                        "customer replies, scheduling, and data summaries. Users launch agents "
                        "from a dashboard, watch live task progress, and review outputs — "
                        "designed to show clear product impact, not just chat demos."
                    ),
                    stack=["React", "Django", "Python", "LLM APIs", "Redis", "WebSockets"],
                    features=[
                        "Specialized AI agents",
                        "Live task progress",
                        "Knowledge-base tools",
                        "Human approval steps",
                    ],
                    live_url="https://example.com",
                    repo_url="https://github.com",
                    image_url="/images/projects/aether-ai-agents.png",
                    accent="#0F766E",
                    featured=True,
                    year="2025",
                    order=4,
                ),
                Project(
                    title="CareAssist Agent",
                    slug="careassist-agent",
                    category="ai",
                    summary="AI agent that triages patient questions before live doctor consults.",
                    description=(
                        "An intake AI agent for telehealth: patients describe symptoms, "
                        "the agent gathers structured history, suggests urgency level, "
                        "and hands a clean brief to the doctor before the live call starts."
                    ),
                    stack=["React", "Django", "LLM APIs", "PostgreSQL"],
                    features=[
                        "Symptom intake chat",
                        "Urgency scoring",
                        "Doctor brief export",
                        "Works with MediLink Live",
                    ],
                    live_url="https://example.com",
                    repo_url="https://github.com",
                    image_url="/images/projects/careassist-agent.png",
                    accent="#0E7490",
                    featured=True,
                    year="2025",
                    order=5,
                ),
                Project(
                    title="Voyage Concierge Agent",
                    slug="voyage-concierge-agent",
                    category="ai",
                    summary="Travel AI agent that recommends boats, hotels, and ticket bundles.",
                    description=(
                        "A concierge-style AI agent for travel agencies and Smagua-style apps. "
                        "It understands destination, budget, and dates, then proposes boat trips, "
                        "hotel stays, and ticket options with bookable links."
                    ),
                    stack=["React", "Django", "LLM APIs", "Maps APIs"],
                    features=[
                        "Trip planning chat",
                        "Boat + hotel suggestions",
                        "Budget-aware options",
                        "One-click booking handoff",
                    ],
                    live_url="https://example.com",
                    repo_url="https://github.com",
                    image_url="/images/projects/voyage-concierge-agent.png",
                    accent="#0369A1",
                    featured=True,
                    year="2024",
                    order=6,
                ),
            ]
        )

        Education.objects.bulk_create(
            [
                Education(
                    institution="University of Engineering & Technology",
                    degree="BS Computer Science",
                    field="Software Engineering",
                    start_year="2015",
                    end_year="2019",
                    details="Focus on distributed systems, databases, and HCI.",
                    order=1,
                ),
                Education(
                    institution="Professional Certifications",
                    degree="Cloud & Backend Specializations",
                    field="AWS · Django · React Advanced",
                    start_year="2020",
                    end_year="2024",
                    details="Continuous upskilling across modern full-stack stacks.",
                    order=2,
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS("Portfolio seed data loaded."))
