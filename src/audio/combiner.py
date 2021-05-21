import sox
import numpy as np
from typing import List
from audio.audio_array import AudioArray
from audio.audio_source import AudioSource

# yaml object
# ---
# type: Combiner
# combine_type: 'mix-power' # or... concatenate merge mix multiply see https://pysox.readthedocs.io/en/latest/api.html#sox.combine.Combiner.build
# inputs:
#   - type: AudioFile
#     filepath: audio.mp3
#   - type: Phaser
#     input:
#       type: AudioFile
#       filepath: audio.mp3
#     gain_in: 0.8
#     gain_out: 0.74
#     delay: 3
#     decay: 0.4
#     speed: 0.5
#     modulation_shape: sinusoidal # or triangular
#   - type: Pitch
#     input:
#       type: AudioFile
#       filepath: audio.mp3
#     amount: 1

class Combiner(AudioSource):
    def __init__(self, inputs: List[AudioSource], combine_type: str='mix-power') -> None:
        super().__init__()
        self.__inputs = inputs
        self.__combine_type = combine_type

    def get_array(self) -> AudioArray:
        combiner = sox.Combiner()
        input_files = [input.get_temp_file() for input in self.__inputs]
        combiner.build(
            input_filepath_list=input_files, 
            output_filepath=self._temp_filepath, 
            combine_type=self.__combine_type
            )
        return AudioArray(
            array=sox.Transformer().build_array(input_filepath=self._temp_filepath),
            sample_rate=sox.file_info.sample_rate(input_filepath=self._temp_filepath)
        )

