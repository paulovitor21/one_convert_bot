import os
import logging
import yt_dlp
import uuid

# configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def download_audio(url, output_dir="downloads"):
    try:
        os.makedirs(output_dir, exist_ok=True)
        temp_id = str(uuid.uuid4())
        output_template = os.path.join(output_dir, f'{temp_id}.%(ext)s')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': True,
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'audio')


        mp3_path = os.path.join(output_dir, f"{temp_id}.mp3")
        if os.path.isfile(mp3_path):
            logging.info(f"Arquivo gerado: {mp3_path}")
            return mp3_path, title
        else:
            logging.warning(f"Arquivo mp3 nao encontrado: {mp3_path}")
            return None, None

    except Exception as e:
        logging.error(f'Erro ao baixar audio: {e}')
        return None, None
