import os

from argparse import ArgumentParser
from pydub import AudioSegment
from os.path import join, exists


def get_audio_paths(base_dir):
    files_list = os.listdir(base_dir)
    return [file for file in files_list
                  if "mp3" in file]


def convert_mp3_to_wav(mp3_path, out_dir, wav_name):
    audio = AudioSegment.from_mp3(mp3_path)
    if not exists(out_dir):
        os.mkdir(out_dir)
    audio.export(os.path.join(out_dir, wav_name))


def convert_audios(args):
    audio_paths = get_audio_paths(args.base_dir)
    for mp3_name in audio_paths:
        wav_name = mp3_name.replace("mp3", "wav")
        mp3_path = join(args.base_dir, mp3_name)
        convert_mp3_to_wav(mp3_path, args.out_dir, wav_name)


parser = ArgumentParser()
parser.add_argument("--base_dir",
                    required=True)
parser.add_argument("--out_dir",
                    required=True)


if __name__ == "__main__":
    args = parser.parse_args()
    convert_audios(args)

