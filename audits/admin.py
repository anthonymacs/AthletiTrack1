# audits/admin.py
from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    """
    Customizes the display of the AuditLog model in the Django admin.
    """
    # Fields to display in the main list view
    list_display = ('timestamp', 'user', 'action', 'details')

    # Fields to allow filtering by
    list_filter = ('action', 'user')

    # Fields to allow searching
    search_fields = ('user__username', 'action', 'details')

    # Make the admin panel read-only. Audit logs should not be editable.
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False