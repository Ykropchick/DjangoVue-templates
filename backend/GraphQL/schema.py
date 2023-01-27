import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from .models import TestGraphQL
from UserExtends.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class TestType(DjangoObjectType):
    class Meta:
        model = TestGraphQL


class TestInput(graphene.InputObjectType):
    field1 = graphene.Int()
    field2 = graphene.Int()


class CreateUser(graphene.Mutation):
    class Arguments:
        input = TestInput(required=True)

    ok = graphene.Boolean()
    test = graphene.Field(TestType)
    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        test = TestGraphQL(field1=input.field1, field2=input.field1)
        test.save()
        return CreateUser(ok=ok, test=test)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.ObjectType):
    tests = graphene.List(TestType)
    test = graphene.List(TestType, id=graphene.Int())

    users = graphene.List(UserType)
    user = graphene.List(UserType, id=graphene.Int())

    def resolve_tests(self, info, **kwargs):
        return TestGraphQL.objects.all()

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_test(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return [TestGraphQL.objects.get(pk=id)]
        return None

    def resolve_user(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return [User.objects.get(pk=id)]
        return None


schema = graphene.Schema(query=Query, mutation=Mutation)