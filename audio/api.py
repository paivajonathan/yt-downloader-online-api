from ninja import Router
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from .schemas import AudioIn, AudioOut, ErrorSchema


router = Router(tags=['Audio'])

@router.post(
    path='download/',
    response={
        201: AudioOut,
        400: ErrorSchema,
        500: ErrorSchema,
    }
)
def download(request, payload: AudioIn):
    try:
        audio = YouTube(payload.url).streams.filter(only_audio=True).first()
        new_filename = audio.default_filename.replace(' ', '_')
        output_path = '/media/audio/'

        audio.download(
            output_path=f'.{output_path}',
            filename=new_filename,
        )
        
        response = {
            'filename': new_filename,
            'path': f'{output_path}{new_filename}',
        }
        return 201, response
    except RegexMatchError:
        return 400, {'msg': 'The given URL doesn\'t match any YouTube audio.'}
    except Exception:
        return 500, {'msg': 'A server error occurred.'} 
