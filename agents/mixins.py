from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import reverse


class OrganizerAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and an organizer."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return reverse('leads:lead-list')
        return super().dispatch(request, *args, **kwargs)
