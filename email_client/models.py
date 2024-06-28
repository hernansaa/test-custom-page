from django.db import models

from django_mailbox.models import Message as BaseMessage
from django_mailbox.models import MessageAttachment as BaseMessageAttachment
from django_mailbox.models import Mailbox

# Create your models here.

class SentEmail(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.recipient} on {self.sent_at}"


class Mailbox(Mailbox):
    class Meta:
        proxy = True

    # Add custom methods or fields as needed


class Message(BaseMessage):
    class Meta:
        proxy = True
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    def custom_method(self):
        # Add any custom methods or properties here
        return "This is a custom method for Message"



class MessageAttachment(BaseMessageAttachment):
    class Meta:
        proxy = True
        verbose_name = 'Message Attachment'
        verbose_name_plural = 'Messages Attachements'
    
    def custom_method(self):
        # Add any custom methods or properties here
        return "This is a custom method for Message"

