import sox
from audio.audio_array import AudioArray
from audio.audio_transform import AudioTransform

# yaml object
# ---
# type: Pitch
# input:
#   type: AudioFile
#   filepath: audio.mp3
# amount: 1

class Pitch(AudioTransform):
    def __init__(self, input, amount) -> None:
        super().__init__(input)
        self.__amount = amount

    def get_array(self) -> AudioArray:
        pitch = sox.Transformer()
        pitch.pitch(self.__amount)
        audio_array = self._input.get_array()
        return AudioArray(
            array=pitch.build_array(
                input_array=audio_array.array,
                sample_rate_in=audio_array.sample_rate
            ),
            sample_rate=audio_array.sample_rate
        )