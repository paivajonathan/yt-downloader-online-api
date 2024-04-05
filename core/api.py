from ninja import NinjaAPI


api = NinjaAPI()

api.add_router('video/', 'video.api.router')
api.add_router('audio/', 'audio.api.router')
