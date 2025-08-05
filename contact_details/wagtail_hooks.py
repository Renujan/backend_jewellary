from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel
from .models import Contact


class ContactViewSet(SnippetViewSet):
    model = Contact
    icon = "comment"
    inspect_view_enabled = True
    add_to_admin_menu = True
    list_display = ("subject", "name","created_at")
    list_export = ("subject","name","email","created_at")
    
    
    list_filter = ("email", "name")
    search_fields = ("subject", "question", "response")
    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('subject'),
        FieldPanel('Message'),
    ]


register_snippet(ContactViewSet)
