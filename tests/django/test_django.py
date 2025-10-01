import pytest
from django.apps import apps

from domain_events.django import DomainEventsConfig


def test_app_config_name():
    class PathedDomainEventsConfig(DomainEventsConfig):
        path = "."

    config = PathedDomainEventsConfig("domain_events", "domain_events")
    assert config.name == "domain_events"
    assert config.verbose_name == "Domain Events System"


@pytest.mark.django_db
def test_ready_triggers_setup_events(monkeypatch):
    called = {}
    monkeypatch.setattr("domain_events.config.setup_events", lambda: called.setdefault("setup", True))
    config = DomainEventsConfig("domain_events", "domain_events")
    config.ready()
    assert called.get("setup") is True
