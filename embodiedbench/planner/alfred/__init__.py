"""Alfred Task Planners"""

def __getattr__(name):
    if name == 'AlfredBasePlanner':
        from .base import VLMPlanner
        return VLMPlanner
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = ['AlfredBasePlanner']

