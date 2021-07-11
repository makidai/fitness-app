import graphene
from graphene_django import DjangoObjectType, DjangoListField
from graphql_jwt.decorators import login_required
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class UserQueries(graphene.ObjectType):
	user = graphene.Field(UserType)