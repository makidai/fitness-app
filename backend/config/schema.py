import graphene
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
	pass

schema = graphene.Schema(query=Query, mutation=Mutation)