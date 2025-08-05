from django.db import models
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.images.models import Image

class ItemExtraImages(models.Model):
    invoice = ParentalKey(
        'Items',
        on_delete=models.CASCADE,
        related_name='item_extra_images'
    )
    photo = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        FieldPanel("photo"),
    ]
    def __str__(self):
        return self.description


class Items(index.Indexed, ClusterableModel):
    COLOUR_CHOICES = [
    ("wild-berry", "Wild Berry"),
    ("dirty-blue", "Dirty Blue"),
    ("sage", "Sage"),
    ("terra-cotta", "Terra Cotta"),
    ("rodeo-dust", "Rodeo Dust"),
    ("como-green", "Como Green"),
    ("grey-goose", "Grey Goose"),
    ("rose-gold", "Rose Gold"),
    ("gold", "Gold"),
    ("black", "Black"),
    ("cyan", "Cyan"),
    ("dark-grey", "Dark Grey"),
    ("carbon-grey", "Carbon Grey"),
    ("white", "White"),
    ("soft-antique", "Soft Antique"),
    ]
    CATEGORY_CHOICES = [
    ("Diamond_Earring", "Diamond Earring"),
    ("Chains", "Chains"),
    ("Necklaces", "Necklaces"),
    ("Diamond_Necklace", "Diamond Necklace"),
    ("Diamond_Bracelet", "Diamond Bracelet"),
    ("Diamond_Bangles", "Diamond Bangles "),
    ("Chokers", "Chokers "),
    ]

    STATUS_CHOICES = [
    ("on-sale", "On Sale"),
    ("in-tock", "In Stock"),
    ]


    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(choices=COLOUR_CHOICES)
    category = models.CharField(choices=CATEGORY_CHOICES)
    status = models.CharField(choices=STATUS_CHOICES)
    description = models.TextField()
    addional_info = models.TextField(null=True, blank=True)
    photo = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
