from django.db import models
from django.utils.translation import gettext as _
from autoslug import AutoSlugField
from slugify import slugify
from apps.users.models import User


# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='user',
        blank=True, 
        null=True
    )
    title = models.CharField(
        _('Title'),
        max_length=50,
        unique=True,
    )
    image = models.ImageField(
        upload_to='category-img',
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        null=True
    )
    cat_slug = AutoSlugField(
        _('Slug'),
        populate_from='title',
        unique=True
    ) 
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now=True, 
        null=True, 
        blank=True
    )
    updated_at = models.DateTimeField(
        _('Upadated at'),
        auto_now=True, 
        null=True, 
        blank=True
    )
    is_deleted = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.cat_slug = slugify(self.title)
        super().save(*args, **kwargs)


class OlympicGame(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=50,
        unique=True,
    )
    thumbnail_image = models.ImageField(
        _('Thumbnail Image'),
        upload_to='category-img',
    )
    video_url = models.URLField(
        _('Video URL'),
    ) 
    description = models.TextField(
        _('Description'),
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='game_category'
    )
    slug = AutoSlugField(
        _('Slug'),
        populate_from='title',
        unique=True
    )
    start_date = models.DateTimeField(
        _('Start date'),
        null=True, 
        blank=True
    )
    end_date = models.DateTimeField(
        _('End date'),
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now=True, 
        null=True, 
        blank=True
    )
    updated_at = models.DateTimeField(
        _('Upadated at'),
        auto_now=True, 
        null=True, 
        blank=True
    )
    is_deleted = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title


class FeaturedCategory(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='user_featuredcategory',
        blank=True, 
    )
    category = models.ManyToManyField(
        Category, 
        related_name='category_featured',
        blank=True, 
    )

    def __str__(self):
        return self.user.first_name
