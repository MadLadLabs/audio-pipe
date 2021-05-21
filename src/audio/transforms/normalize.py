import sox
from audio.audio_array import AudioArray
from audio.audio_transform import AudioTransform

# yaml object
# ---
# type: Normalize
# input:
#   type: AudioFile
#   filepath: audio.mp3
# db_level: -3

class Normalize(AudioTransform):
    def __init__(self, input, db_level=-3) -> None:
        super().__init__(input)
        self.__db_level = db_level

    def get_array(self) -> AudioArray:
        norm = sox.Transformer()
        norm.norm(self.__db_level)
        audio_array = self._input.get_array()
        return AudioArray(
            array=norm.build_array(
                input_array=audio_array.array,
                sample_rate_in=audio_array.sample_rate
            ),
            sample_rate=audio_array.sample_rate
        )