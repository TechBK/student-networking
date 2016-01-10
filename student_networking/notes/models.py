from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    is_thread = models.BooleanField(default=False)

    def __str__(self):
        return "Name: %s, Thread: %s, Public: %s" % (self.name, self.is_thread, self.is_public)


class Note(models.Model):
    TEXT = 'TE'
    IMAGE = 'IM'
    TEXT_IMAGE = 'TI'
    TEXT_TEXT = 'TT'
    CONTENT_TYPE_CHOICES = (
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
        (TEXT_IMAGE, 'Text_Image'),
        (TEXT_TEXT, 'Text_Text'),
    )
    content_type = models.CharField(max_length=2, choices=CONTENT_TYPE_CHOICES, default=TEXT)
    time = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag)
    user = models.ManyToManyField(User)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return "Type: %s, Time: %s" % (self.content_type, self.time)


class NoteImage(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='%Y/%m/%d/')
    position = models.PositiveSmallIntegerField()


class NoteText(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.TextField()
    position = models.PositiveSmallIntegerField(default=0)
