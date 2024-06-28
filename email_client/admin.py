from django.contrib import admin

from .models import SentEmail, Message, MessageAttachment

class SentEmailAdmin(admin.ModelAdmin):
    list_display = ['subject', 'recipient', 'sent_at']
    search_fields = ['subject', 'recipient']
    list_filter = ['sent_at']



# Extended from django-mailbox by Proxy Models

# Customize admin for CustomMessage
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'from_header', 'to_header', 'outgoing', 'processed', 'read')
    list_filter = ('outgoing', 'processed', 'read')
    search_fields = ('subject', 'from_header', 'to_header', 'body')


# Customize admin for CustomMessage
class MessageAttachmentAdmin(admin.ModelAdmin):
    pass


# Register your models with their respective admin classes
admin.site.register(SentEmail, SentEmailAdmin)

# Register the proxy models 
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageAttachment, MessageAttachmentAdmin)
