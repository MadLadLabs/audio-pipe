import uuid
import sox

from audio.audio_array import AudioArray

class AudioSource:
    def __init__(self) -> None:
        self._temp_filepath = f'/tmp/{str(uuid.uuid4())}.flac'
        if type(self) is AudioSource:
            raise Exception('AudioSource is an abstract class')

    def get_array(self) -> AudioArray:
        raise Exception('get_array is an abstract method of AudioSource and must be overriden in the deriving class')

    def __build_temp_file(self) -> None:
        audio_array = self.get_array()
        sox.Transformer().build_file(
            input_array=audio_array.array, 
            sample_rate_in=audio_array.sample_rate, 
            output_filepath=self._temp_filepath)

    def get_temp_file(self) -> str:
        self.__build_temp_file()
        return self._temp_filepath