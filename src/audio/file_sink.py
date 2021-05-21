import sox
from audio.audio_source import AudioSource

class FileSink:
    def __init__(self, input: AudioSource, filepath: str) -> None:
        self.__input = input
        self.__filepath = filepath

    def save(self) -> None:
        audio_array = self.__input.get_array()
        sox.Transformer().build_file(
            input_array=audio_array.array,
            sample_rate_in=audio_array.sample_rate,
            output_filepath=self.__filepath
            )