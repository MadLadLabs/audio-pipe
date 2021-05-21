from audio.audio_file import AudioFile
from audio.audio_source import AudioSource
from audio.combiner import Combiner
from audio.transforms.bass import Bass
from audio.transforms.normalize import Normalize
from audio.transforms.overdrive import Overdrive
from audio.transforms.phaser import Phaser
from audio.transforms.pitch import Pitch


def hydrate_AudioFile(**kwargs) -> AudioFile:
    return AudioFile(filepath=kwargs['filepath'])

def hydrate_Bass(**kwargs) -> Bass:
    return Bass(
        input=hydrate_AudioSource(**(kwargs['input'])),
        **{k: kwargs[k] for k in kwargs.keys() - {'input'} }
    )

def hydrate_Normalize(**kwargs) -> Normalize:
    return Normalize(
        input=hydrate_AudioSource(**(kwargs['input'])),
        **{k: kwargs[k] for k in kwargs.keys() - {'input'} }
    )

def hydrate_Overdrive(**kwargs) -> Overdrive:
    return Overdrive(
        input=hydrate_AudioSource(**(kwargs['input'])),
        **{k: kwargs[k] for k in kwargs.keys() - {'input'} }
    )

def hydrate_Phaser(**kwargs) -> Phaser:
    return Phaser(
        input=hydrate_AudioSource(**(kwargs['input'])),
        **{k: kwargs[k] for k in kwargs.keys() - {'input'} }
    )

def hydrate_Pitch(**kwargs) -> Pitch:
    return Pitch(
        input=hydrate_AudioSource(**(kwargs['input'])),
        **{k: kwargs[k] for k in kwargs.keys() - {'input'} }
    )

def hydrate_Combiner(**kwargs) -> Combiner:
    return Combiner(
        inputs=[hydrate_AudioSource(**source) for source in kwargs['inputs']],
        **{k: kwargs[k] for k in kwargs.keys() - {'inputs'} }
    )

hydration_mapping = {
    "AudioFile": hydrate_AudioFile,
    "Bass": hydrate_Bass,
    "Normalize": hydrate_Normalize,
    "Overdrive": hydrate_Overdrive,
    "Phaser": hydrate_Phaser,
    "Pitch": hydrate_Pitch,
    "Combiner": hydrate_Combiner
}

def hydrate_AudioSource(**kwargs) -> AudioSource:
    return hydration_mapping[kwargs['type']](**{k: kwargs[k] for k in kwargs.keys() - {'type'} })