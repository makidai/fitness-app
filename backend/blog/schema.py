import graphene
import graphene_django_optimizer as gql_optimizer
from graphene_django import DjangoObjectType
from .models import Post, Category, Tag


class PostType(DjangoObjectType):
	class Meta:
		model = Post


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

	def resolve_posts(self, info, **kwargs):
		qs = Post.objects.all()
		return gql_optimizer.query(qs, info)

	def resolve_categories(self, info, **kwargs):
		qs = Category.objects.all()
		return gql_optimizer.query(qs, info)

	def resolve_tags(self, info, **kwargs):
		qs = Tag.objects.all()
		return gql_optimizer.query(qs, info)