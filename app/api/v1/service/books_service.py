from typing import List

from boto3.dynamodb.conditions import Key

from .db import session
from ..model.book import Book

table = session.Table('Books')


def get_book(title: str, author: str) -> Book:
    result = table.get_item(Key={"Author": author, "Title": title})
    return Book.parse_obj(result['Item'])


def get_books_by_author(author: str) -> List[Book]:
    query_key = Key('Author').eq(author)
    result = table.query(KeyConditionExpression=query_key)
    return [Book.parse_obj(item) for item in result['Items']]


def create_book(book: Book) -> None:
    table.put_item(Item=book.dict(by_alias=True))


def create_books(books: List[Book]) -> None:
    with table.batch_writer() as batch:
        for book in books:
            batch.put_item(Item=book.dict())


def update_book(book: Book) -> Book:
    result = table.update_item(
        Key={"Author": book.author, "Title": book.title},
        ExpressionAttributeNames={
            "#formats": "Formats",
            "#category": "Category"
        },
        ExpressionAttributeValues={
            ":new_for": book.formats,
            ":new_cat": book.category
        },
        UpdateExpression="SET #formats = :new_for, #category = :new_cat",
        ReturnValues="UPDATED_NEW"
    )
    return Book.parse_obj(result['Attributes'])


def delete_book(title: str, author: str) -> None:
    table.delete_item(Key={"Author": author, "Title": title})
