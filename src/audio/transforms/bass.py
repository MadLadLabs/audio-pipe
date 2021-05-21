import sox
from audio.audio_array import AudioArray
from audio.audio_transform import AudioTransform

# yaml object
# ---
# type: Bass
# input:
#   type: AudioFile
#   filepath: audio.mp3
# gain_db: 5
# frequency: 100
# slope: 0.5

class Bass(AudioTransform):
    def __init__(self, input, 
    gain_db,
    frequency=100,
    slope=0.5,
    ) -> None:
        super().__init__(input)
        self.__gain_db = gain_db
        self.__frequency = frequency
        self.__slope = slope

    def get_array(self) -> AudioArray:
        bass = sox.Transformer()
        bass.bass(
            slope=self.__slope,
            gain_db=self.__gain_db,
            frequency=self.__frequency,
        )
        audio_array = self._input.get_array()
        return AudioArray(
            array=bass.build_array(
                input_array=audio_array.array,
                sample_rate_in=audio_array.sample_rate
            ),
            sample_rate=audio_array.sample_rate
        )