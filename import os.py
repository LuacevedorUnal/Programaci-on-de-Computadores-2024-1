import os
import shutil

def organize_files(root_dir):
    # Create folders for each file type
    doc_dir = os.path.join(root_dir, 'Documentos')
    img_dir = os.path.join(root_dir, 'Imágenes')
    audio_dir = os.path.join(root_dir, 'Archivos de audio')
    video_dir = os.path.join(root_dir, 'Vídeos')
    misc_dir = os.path.join(root_dir, 'Misceláneos')

    # Create folders if they don't exist
    os.makedirs(doc_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(misc_dir, exist_ok=True)

    # Iterate over files in the root directory
    for entry in os.scandir(root_dir):
        if entry.is_file():
            filepath = entry.path
            # Determine file type
            if filepath.endswith(('.txt', '.doc', '.docx', '.pdf')):
                shutil.move(filepath, doc_dir)
            elif filepath.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                shutil.move(filepath, img_dir)
            elif filepath.endswith(('.mp3', '.wav', '.ogg')):
                shutil.move(filepath, audio_dir)
            elif filepath.endswith(('.mp4', '.avi', '.mov')):
                shutil.move(filepath, video_dir)
            else:
                shutil.move(filepath, misc_dir)

# Organize files in the "Descargas" folder
root_dir = 'C:\\Users\\felip\\Descargas'
organize_files(root_dir)

# Organize files in the "Escritorio" folder
root_dir = 'C:\\Users\\felip\\Escritorio'
organize_files(root_dir)