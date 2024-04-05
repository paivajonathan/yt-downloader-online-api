from ninja.router import Router
from pytube import YouTube
from pytube.exceptions import RegexMatchError

from .schemas import VideoSchemaIn, VideoSchemaOut, ErrorSchema
import ffmpeg


router = Router(tags=['Video'])

@router.post(
    path='download/',
    response={
        201: VideoSchemaOut,
        400: ErrorSchema,
        500: ErrorSchema,
    },
)
def download(request, payload: VideoSchemaIn):
    try:
        video = (
            YouTube(payload.url)
            .streams
            .filter(file_extension='mp4')
            .order_by('resolution')
            .desc()
            .first()
        )
        new_filename = video.default_filename.replace(' ', '_')
        output_path = '/media/video/'
        
        video.download(
            output_path=f'.{output_path}',
            filename=new_filename,
        )
        
        response = {
            'filename': new_filename,
            'path': f'{output_path}{new_filename}',
        }
        return 201, response
    except RegexMatchError:
        return 400, {'msg': 'The given URL doesn\'t match any YouTube video.'}
    except Exception:
        return 500, {'msg': 'A server error occurred.'} 
