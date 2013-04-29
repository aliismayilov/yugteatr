from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Language(models.Model):
    name = models.SlugField(max_length=10, unique=True)
    order = models.IntegerField(null=True, blank=True) # optional order field

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s' % self.name


class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    language = models.ForeignKey('Language')

    url = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(null=True, blank=True) # optional order field

    # parent page
    parent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return '/%s/%s.html' % (self.language, self.slug)


class Actor(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    photo = ThumbnailerImageField(upload_to='actors', blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/actors/%s' % self.slug


class Play(models.Model):
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.slug


class PlayPhoto(models.Model):
    title = models.CharField(max_length=50)
    photo = ThumbnailerImageField(upload_to='plays')
    play = models.ForeignKey('Play')

    def __unicode__(self):
        return self.title


class PlayInformation(models.Model):
    play = models.ForeignKey('Play')
    language = models.ForeignKey('Language')

    title = models.CharField(max_length=50)
    body = models.TextField()

    def __unicode__(self):
        return self.title


class Performance(models.Model):
    play = models.ForeignKey('Play')
    show_time = models.DateTimeField()

    def __unicode__(self):
        return '%s - %s' % (self.play.slug, self.show_time.strftime('%d.%b.%Y'))
