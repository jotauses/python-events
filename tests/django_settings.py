SECRET_KEY = "dummy"
INSTALLED_APPS = [
    "domain_events.django",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
