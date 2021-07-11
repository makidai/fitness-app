import graphene
from graphene_django import DjangoObjectType, DjangoListField
from graphql_jwt.decorators import login_required
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
	user = graphene.Field(UserType)

	class Arguments:
		username = graphene.String(required=True)
		password = graphene.String(required=True)

	def mutate(self, info, username, password):
		user = get_user_model()(username=username)
		user.set_password(password)
		user.save()
		return CreateUser(user=user)


class UserQueries(graphene.ObjectType):
	user = graphene.Field(UserType)


class UserMutations(graphene.ObjectType):
	create_user = CreateUser.Field()