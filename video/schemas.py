from ninja.schema import Schema


class VideoSchemaIn(Schema):
    url: str


class VideoSchemaOut(Schema):
    title: str
    path: str


class ErrorSchema(Schema):
    msg: str
