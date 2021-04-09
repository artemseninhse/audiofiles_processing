import os

from argparse import ArgumentParser
from pydub import AudioSegment
from os.path import join, exists
from utils import CONVERTED_DIR


def get_audio_paths(args):
    files_list = os.listdir(args.base_dir)
    frmt = "mp3" if args.mp3 else "wav"
    return [file for file in files_list
            if file.endswith(frmt)]


def convert_mp3_to_wav(base_dir,
                       mp3_path,
                       wav_name):
    audio = AudioSegment.from_mp3(join(base_dir, mp3_path))
    out_dir = join(base_dir, CONVERTED_DIR)
    if not exists(out_dir):
        os.mkdir(out_dir)
    audio.export(os.path.join(out_dir, wav_name))


def convert_batch(args):
    audio_paths = get_audio_paths(args)
    for mp3_name in audio_paths:
        wav_name = mp3_name.replace("mp3", "wav")
        convert_mp3_to_wav(args.base_dir,
                           mp3_name,
                           wav_name)


parser = ArgumentParser()
parser.add_argument("--mp3",
                    required=False,
                    default=False,
                    action="store_true")
parser.add_argument("--base_dir",
                    required=True)


if __name__ == "__main__":
    args = parser.parse_args()
    convert_batch(args)

