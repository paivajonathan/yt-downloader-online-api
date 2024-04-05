from ninja import Schema


class AudioIn(Schema):
    url: str


class AudioOut(Schema):
    filename: str
    path: str


class ErrorSchema(Schema):
    msg: str
