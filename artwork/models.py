from django.db import models
from django.utils.html import mark_safe
from userauths.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from shortuuid.django_fields import ShortUUIDField

STATUS = (
	("draft", "Draft"),
	("disabled", "Disabled"),
	("rejected", "Rejected"),
	("in_review", "In Review"),
	("published", "Published"),
)

class Category(models.Model):
	cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix='cat', alphabet='abcdefgh12345')
	title = models.CharField(max_length=100, default="Category Name")

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title

class Post(models.Model):
	pid = ShortUUIDField(unique=True, length=10, max_length=30, alphabet='abcdefgh12345')

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	categories = models.ManyToManyField(Category, related_name="categories")

	tags = TaggableManager(blank=True)

	image = models.ImageField(upload_to='blog', default="blog.jpg")
	title = models.CharField(max_length=100, default="Post Name")
	subtitle = models.TextField(null=True, blank=True, default="Post Subtitle")
	
	body = RichTextUploadingField(null=True, blank=True, default="Post Body")

	post_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Posts'

	def blog_image(self):
		return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

	def __str__(self):
		return self.title

class PostImages(models.Model):
	images = models.ImageField(upload_to="post-images", default="post.jpg")
	post = models.ForeignKey(Post, related_name="p_images", on_delete=models.SET_NULL, null=True)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Post Images'




class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	body = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Comments'

	def __str__(self):
		return self.post.title

class ContactUs(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	message = models.TextField()

	class Meta:
		verbose_name = 'Contact Us'
		verbose_name_plural = 'Contact Us'

	def __str__(self):
		return self.name

class ArtistBio(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True, blank=True, default="Product Description")
    images = models.ImageField(upload_to='artist_bio_images/', null=True, blank=True)

class Resume(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True, blank=True, default="Product Description")
    images = models.ImageField(upload_to='resume_images/', null=True, blank=True)

class ArtistStatement(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True, blank=True, default="Product Description")
    images = models.ImageField(upload_to='artist_statement_images/', null=True, blank=True)

class ArtistPortfolio(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True, blank=True, default="Product Description")
    images = models.ImageField(upload_to='artist_portfolio_images/', null=True, blank=True)