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
    body = models.TextField(null=True, blank=True)
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




class Person(models.Model):
    slug = models.SlugField(max_length=50)

    photo = ThumbnailerImageField(upload_to='performers', blank=True, null=True)

    # enum type field
    PERFORMER = 1
    DESIGNER = 2
    DIRECTOR = 3
    PERSON_TYPES = (
        (PERFORMER, 'Performer'),
        (DESIGNER, 'Designer'),
        (DIRECTOR, 'Director'),
    )
    staff_type = models.IntegerField(choices=PERSON_TYPES)

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return '/performers/%s' % self.slug

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'


class PersonInformation(models.Model):
    language = models.ForeignKey('Language')
    name = models.CharField(max_length=50)
    about = models.TextField()

    def __unicode__(self):
        return self.name


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
    
    performers = models.ManyToManyField('Person', related_name='performers')
    designers = models.ManyToManyField('Person', related_name='designers')
    directors = models.ManyToManyField('Person', related_name='directors')

    def __unicode__(self):
        return '%s - %s' % (self.play.slug, self.show_time.strftime('%d.%b.%Y'))

    class Meta:
        ordering = ['-show_time']

    def get_playinformation(self, language):
        return self.play.playinformation_set.get(language=language)
