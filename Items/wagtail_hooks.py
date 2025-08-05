from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel,InlinePanel
from .models import Items


class ItemsViewSet(SnippetViewSet):
    model = Items
    icon = "help"
    inspect_view_enabled = True
    add_to_admin_menu = True
    list_display = ("name","price",'discount',"color","status")
    list_export = ("name","price","color","status","description","created_at")
    
    list_filter = ("name", "color","status","created_at")
    search_fields = ("name")
    panels = [
        FieldPanel('name'),
        FieldPanel('price'),
        FieldPanel('discount'),
        FieldPanel('color'),
        FieldPanel('category'),
        FieldPanel('addional_info'),
        FieldPanel('status'),
        FieldPanel('description'),
        FieldPanel('photo'),
        InlinePanel("item_extra_images", label="Extra Photos"),
    ]


register_snippet(ItemsViewSet)
