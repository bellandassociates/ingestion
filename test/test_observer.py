# -*- coding: utf-8 -*-

from unittest.mock import MagicMock, patch
from watchdog.events import FileCreatedEvent
from ingestion.observer import EventHandler

@patch("watchdog.observers.Observer")
def test_observer_launch(INCOMING_PATH, mock_observer_cls):
    """
    Test that the observer process launches and persists.
    """
    fake_observer = MagicMock()
    mock_observer_cls.return_value = fake_observer
    observer = start_observer(INCOMING_PATH)
    mock_observer_cls.assert_called_once()
    observer.schedule.assert_called_once_with(INCOMING_PATH, recursive=False)
    observer.start.assert_called_once()

    assert observer is fake_observer
    pass

def test_handler_detects_file_and_triggers_event():
    """
    Test that the handler triggers and event when a file is detected in the
    watched directory.
    """
    pass

def test_handler_calls_processor_based_on_file_type():
    """
    Test that the handler launches processor based on detected file type.
    """
    pass

# EOF
