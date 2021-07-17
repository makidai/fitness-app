import graphene
import graphql_jwt
from account.schema import (
	UserQueries,
	UserMutations
)
from blog.schema import (
	BlogQueries,
)

class Query(
	UserQueries,
	BlogQueries,
	graphene.ObjectType):
	pass


class Mutation(
	UserMutations,
	graphene.ObjectType):
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)