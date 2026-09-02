from django.contrib import admin
from .models import Contact, GalleryImage
from .models import Visitor

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "mobile",
        "subject",
        "message",
        "status",
        "created_at",
    )

    list_display_links = (
        "name",
        "subject",
    )

    search_fields = (
        "name",
        "email",
        "mobile",
        "subject",
        "message",
    )

    list_filter = (
        "status",
        "created_at",
    )

    ordering = (
        "-created_at",
    )






@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'is_active',
        'order',
        'created_at',
    )

    list_filter = (
        'category',
        'is_active',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
    )

    list_editable = (
        'is_active',
        'order',
    )

    ordering = (
        'order',
        '-created_at',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (
        (
            'Image Information',
            {
                'fields': (
                    'title',
                    'image',
                    'description',
                )
            }
        ),

        (
            'Gallery Category',
            {
                'fields': (
                    'category',
                )
            }
        ),

        (
            'Display Settings',
            {
                'fields': (
                    'is_active',
                    'order',
                )
            }
        ),

        (
            'Timestamps',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                ),
                'classes': ('collapse',),
            }
        ),
    )





@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):

    list_display = (
        "ip_address",
        "visit_date",
        "visit_time",
    )

    list_filter = (
        "visit_date",
    )

    search_fields = (
        "ip_address",
    )

    ordering = (
        "-visit_time",
    )
