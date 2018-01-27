from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["first_name", "updated", "timestamp"]
	#list_display = ["last_name", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["first_name"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["first_name", "last_name"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)