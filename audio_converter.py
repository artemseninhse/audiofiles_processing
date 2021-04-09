import os

from argparse import ArgumentParser
from pydub import AudioSegment
from os.path import join, exists


def get_audio_paths(base_dir, frmt):
    files_list = os.listdir(base_dir)
    return [file for file in files_list
            if file.endswith(frmt)]


def convert_mp3_to_wav(mp3_path, out_dir, wav_name):
    audio = AudioSegment.from_mp3(mp3_path)
    if not exists(out_dir):
        os.mkdir(out_dir)
    audio.export(os.path.join(out_dir, wav_name))


def convert_batch(args):
    audio_paths = get_audio_paths(args.base_dir,
                                  args.frmt)
    for mp3_name in audio_paths:
        wav_name = mp3_name.replace("mp3", "wav")
        filepath = join(args.base_dir, mp3_name)
        convert_mp3_to_wav(filepath, args.out_dir, wav_name)


parser = ArgumentParser()
parser.add_argument("--frmt",
                    required=False,
                    default="mp3")
parser.add_argument("--base_dir",
                    required=True)
parser.add_argument("--out_dir",
                    required=True)


if __name__ == "__main__":
    args = parser.parse_args()
    convert_batch(args)

