import graphene
import graphene_django_optimizer as gql_optimizer
from graphene_django import DjangoObjectType
from datetime import datetime
from .models import Post, Category, Tag, Collection


class CollectionType(DjangoObjectType):
	class Meta:
		model = Collection


class PostType(DjangoObjectType):
	collections = graphene.List(CollectionType, required=True)
	date = graphene.String(required=True)
	class Meta:
		model = Post
		fields = [
		'id',
		'category',
		'tags',
		'title',
		'content',
		'description',
		'image',
		]

	def resolve_collections(self, _info, **kwargs):
		return [collection for collection in self.collections.all()]

	def resolve_date(self, _info, **kwargs):
		return self.updated_at.strftime('%Y-%m-%d')


class CategoryType(DjangoObjectType):
	class Meta:
		model = Category


class TagType(DjangoObjectType):
	class Meta:
		model = Tag




class BlogQueries(graphene.ObjectType):
	posts = graphene.List(PostType)
	categories = graphene.List(CategoryType)
	tags = graphene.List(TagType)
	collections = graphene.List(CollectionType)

	def resolve_posts(self, info, **kwargs):
		qs = Post.objects.all()
		return gql_optimizer.query(qs, info)

	def resolve_categories(self, info, **kwargs):
		qs = Category.objects.all()
		return gql_optimizer.query(qs, info)

	def resolve_tags(self, info, **kwargs):
		qs = Tag.objects.all()
		return gql_optimizer.query(qs, info)

	def resolve_collections(self, info, **kwargs):
		qs = Collection.objects.all()
		return gql_optimizer.query(qs, info)