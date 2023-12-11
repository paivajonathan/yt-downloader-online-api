from ninja import Schema


class AudioIn(Schema):
    url: str


class AudioOut(Schema):
    title: str
    path: str


class ErrorSchema(Schema):
    msg: str
