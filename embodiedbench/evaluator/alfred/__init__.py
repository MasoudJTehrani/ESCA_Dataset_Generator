"""Alfred Task Evaluators"""

def __getattr__(name):
    if name == 'AlfredBaseEvaluator':
        from .base import EB_AlfredEvaluator
        return EB_AlfredEvaluator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = ['AlfredBaseEvaluator']

