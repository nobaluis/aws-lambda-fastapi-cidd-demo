from typing import List

from .db import session
from ..model.book import Book

from boto3.dynamodb.conditions import Key

table = session.Table('Books')


def get_book(title: str, author: str) -> Book:
    result = table.get_item(Key={"Author": author, "Title": title})
    return Book.parse_obj(result['Item'])


def get_books_by_author(author: str) -> List[Book]:
    query_key = Key('Author').eq(author)
    result = table.query(KeyConditionExpression=query_key)
    return [Book.parse_obj(item) for item in result['Items']]
