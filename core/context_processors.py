# core/context_processors.py
from core.models import Sport, Campus

def nav_context(request):
    """
    Provides site-wide context for navigation elements.
    """
    return {
        'all_sports': Sport.objects.all().order_by('name'),
        'all_campuses': Campus.objects.all().order_by('name'),
    }