import os

from os.path import join
from scipy.io import wavfile

AUGMENTED_DIR = "aug_audio"
CONVERTED_DIR = "wav_audio_1204"


def augment_noise(x):
    pass


def augment_volume(x):
    pass


def clear_dir(x):
    for file in os.listdir(x):
        os.remove(join(x, file))


def read_wav(x):
    return wavfile.read(x)

