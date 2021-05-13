import os

from argparse import ArgumentParser
from inspect import (
        Parameter,
        signature
        )
from os.path import (
        isdir,
        join,
        exists
        )
from sox.transform import Transformer


DEFAULT_ARGS = {
            "contrast": [75],
            "speed": [0.9],
            "dcshift": [-1],
            "pad": [1,0]
        }


class AudioAug:
    
    def __init__(self, 
                 transform, 
                 params=[]):
        self.transform = transform
        self.params = params
        if not self.params:
            self.params = DEFAULT_ARGS[self.transform]
    
    def _get_out_path(self,
                      filename,
                      out_dir):
        filename = filename.replace(".wav",
                                    f"_{self.transform}.wav")
        return join(out_dir, filename)

    def transform_audio(self,
                        in_path,
                        out_path):
        tfm = Transformer()
        getattr(tfm, self.transform)(*self.params)
        getattr(tfm, "build")(in_path, out_path)
        arr = tfm.build_array(in_path)

    def apply(self, 
              input_path, 
              out_dir):
        if not exists(out_dir):
            os.mkdir(out_dir)
        if isdir(input_path):
            for filename in os.listdir(input_path):
                in_path = join(input_path,
                                filename)
                out_path = self._get_out_path(filename,
                                              out_dir)
                self.transform_audio(in_path,
                                     out_path)
        else:
            filename = input_path.split("/")[-1]
            out_path = self._get_out_path(filename,
                                          out_dir)
            print(out_path, input_path)
            self.transform_audio(input_path,
                                 out_path)


parser = ArgumentParser()
parser.add_argument("--in_path",
                    required=True)
parser.add_argument("--out_dir",
                    required=True)
parser.add_argument("--transform",
                    required=True)
parser.add_argument("--params",
                    nargs="+",
                    default=[],
                    required=False)


if __name__ == "__main__":
    args = parser.parse_args()
    augmentor = AudioAug(args.transform,
                         [float(i) for i in args.params])
    augmentor.apply(args.in_path,
                    args.out_dir)
