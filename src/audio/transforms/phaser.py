import sox
from audio.audio_array import AudioArray
from audio.audio_transform import AudioTransform

# yaml object
# ---
# type: Phaser
# input:
#   type: AudioFile
#   filepath: audio.mp3
# gain_in: 0.8
# gain_out: 0.74
# delay: 3
# decay: 0.4
# speed: 0.5
# modulation_shape: sinusoidal # or triangular

class Phaser(AudioTransform):
    def __init__(self, input, 
    gain_in=0.8,
    gain_out=0.74,
    delay=3,
    decay=0.4,
    speed=0.5,
    modulation_shape='sinusoidal' # or 'triangular'
    ) -> None:
        super().__init__(input)
        self.__gain_in = gain_in
        self.__gain_out = gain_out
        self.__delay = delay
        self.__decay = decay
        self.__speed = speed
        self.__modulation_shape = modulation_shape

    def get_array(self) -> AudioArray:
        phaser = sox.Transformer()
        phaser.phaser(
            decay=self.__decay,
            delay=self.__delay,
            gain_in=self.__gain_in,
            gain_out=self.__gain_out,
            speed=self.__speed,
            modulation_shape=self.__modulation_shape
        )
        audio_array = self._input.get_array()
        return AudioArray(
            array=phaser.build_array(
                input_array=audio_array.array,
                sample_rate_in=audio_array.sample_rate
            ),
            sample_rate=audio_array.sample_rate
        )