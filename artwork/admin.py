from django.contrib import admin
from artwork.models import Post, Category, Comment, PostImages, ArtistBio, Resume, ArtistStatement, ArtistPortfolio

class PostImagesAdmin(admin.TabularInline):
	model = PostImages

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImagesAdmin]
    list_display = ['title', 'blog_image', 'pid']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'cid']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['user', 'post']
 
 
@admin.register(ArtistBio)
class ArtistBioAdmin(admin.ModelAdmin):
    list_display = ['title']  # Customize the displayed fields as needed

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title']  # Customize the displayed fields as needed

@admin.register(ArtistStatement)
class ArtistStatementAdmin(admin.ModelAdmin):
    list_display = ['title']  # Customize the displayed fields as needed

@admin.register(ArtistPortfolio)
class ArtistPortfolioAdmin(admin.ModelAdmin):
    list_display = ['title']  # Customize the displayed fields as needed

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
