'''
Model of a blog post
'''
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone

# Create your models here.

USER = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    '''Defining custom queryset for the BlogPost model'''
    def published(self):
        '''Returns the blog posts that are published'''
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        '''Searches for blog posts that match certain keywords'''
        lookup = (Q(title__icontains=query)
                  | Q(content__icontains=query)
                  | Q(slug__icontains=query)
                  | Q(user__first_name__icontains=query)
                  | Q(user__last_name__icontains=query)
                  | Q(user__username__icontains=query))
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    '''Manager class for BlogPost model'''
    def get_queryset(self):
        '''Returns queryset'''
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        '''Returns the blog posts that are published'''
        return self.get_queryset().published()

    def search(self, query=None):
        '''Searches for blog posts with the help of custom queryset'''
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model):
    '''Defines the BlogPost model'''

    user = models.ForeignKey(USER,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False,
                                        auto_now_add=False,
                                        null=True,
                                        blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        '''Returns the absolute URL'''
        return f'/blog/{self.slug}'

    def get_edit_url(self):
        '''Returns the URL for edit operation'''
        return f'{self.get_absolute_url()}/edit'

    def get_delete_url(self):
        '''Returns the URL for delete operation'''
        return f'{self.get_absolute_url()}/delete'
