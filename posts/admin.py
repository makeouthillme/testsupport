from django.contrib import admin
from django.contrib.auth.models import Group
from posts.models import Post


class SnippetAdmin(admin.ModelAdmin):
 	list_display = ('name', 'created_on', 'status')
 	list_filter = ('name', 'created_on', 'status')

admin.site.site_header = 'Support admin'
admin.site.register(Post, SnippetAdmin)
admin.site.unregister(Group)
