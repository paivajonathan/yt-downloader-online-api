from ninja import NinjaAPI


api = NinjaAPI()

@api.get('teste/')
def teste():
    return 'teste'

api.add_router('video/', 'video.api.router')
api.add_router('audio/', 'audio.api.router')
