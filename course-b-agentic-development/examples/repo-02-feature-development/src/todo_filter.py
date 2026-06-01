"""Small task-list utilities for Lab 02."""


def list_titles(tasks):
    """Return all task titles in their original order."""
    return [task["title"] for task in tasks]
