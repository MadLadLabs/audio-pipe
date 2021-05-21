from audio.audio_source import AudioSource

class AudioTransform(AudioSource):
    def __init__(self, input: AudioSource) -> None:
        super().__init__()
        self._input = input
        if type(self) is AudioTransform:
            raise Exception('AudioTransform is an abstract class')