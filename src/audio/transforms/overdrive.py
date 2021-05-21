import sox
from audio.audio_array import AudioArray
from audio.audio_transform import AudioTransform

# yaml object
# ---
# type: Overdrive
# input:
#   type: AudioFile
#   filepath: audio.mp3
# gain_db: 20
# colour: 20

class Overdrive(AudioTransform):
    def __init__(self, input, 
    gain_db=20,
    colour=20,
    ) -> None:
        super().__init__(input)
        self.__gain_db = gain_db
        self.__colour = colour

    def get_array(self) -> AudioArray:
        overdrive = sox.Transformer()
        overdrive.overdrive(
            gain_db=self.__gain_db,
            colour=self.__colour,
        )
        audio_array = self._input.get_array()
        return AudioArray(
            array=overdrive.build_array(
                input_array=audio_array.array,
                sample_rate_in=audio_array.sample_rate
            ),
            sample_rate=audio_array.sample_rate
        )