import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from quiz import quiz
from strawberry.field_extensions import InputMutationExtension

# start types

@strawberry.type
class Options:
    a: str

@strawberry.type
class HouseMaping:
    slytherin: str
    ravenclaw: str
    hufflepuff: str
    gryffindor: str

@strawberry.type
class Question:
    order: int
    question: str
    options: Options
    house_maping: HouseMaping

@strawberry.input
class Answers:
    question_number: int
    selected_answer: str


@strawberry.type
class Results:
    house: str
    description: str

# end types

@strawberry.type
class Query:
    @strawberry.field
    def get_quiz(self) -> list[Question]:
        return strawberry.field(resolver=quiz.get_questions())

@strawberry.type
class Mutation:
    @strawberry.mutation
    def sumit_quiz(answers: list[Answers]) -> Results:
        results = quiz.get_results(answers)

        return Results(house=results, description="")


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")