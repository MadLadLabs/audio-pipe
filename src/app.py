import os
import glob
import yaml
from audio.audio_factory import hydrate_AudioSource
from audio.file_sink import FileSink

if __name__ == "__main__":
    os.chdir('/workspace')

    recipe_files = glob.glob('*.yml')

    if not os.path.exists('output'):
        os.mkdir('output')


    for recipe_file in recipe_files:
        filename = os.path.splitext(os.path.basename(recipe_file))[0]
        with open(recipe_file) as f:
            recipe = yaml.load(f, Loader=yaml.FullLoader)

            output = FileSink(
                input=hydrate_AudioSource(**recipe),
                filepath=f'output/{filename}.mp3'
            )

            output.save()

