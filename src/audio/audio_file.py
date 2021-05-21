import sox
from audio.audio_array import AudioArray
from audio.audio_source import AudioSource

# yaml object
# ---
# type: AudioFile
# filepath: audio.mp3


class AudioFile(AudioSource):
    def __init__(self, filepath) -> None:
        super().__init__()
        self.filepath = filepath

    def get_array(self) -> AudioArray:
        return AudioArray(
            array=sox.Transformer().build_array(input_filepath=self.filepath),
            sample_rate=sox.file_info.sample_rate(input_filepath=self.filepath)
        )