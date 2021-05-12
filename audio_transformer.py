import os
import sox

from sox.transform import Transformer


class AudioAug(Transformer):

    def __init__(self, 
                 transform, 
                 params):
        super(AudioAug, self).__init__()
        self.transform = transform
        self.params = params
        
    def apply(self, in_path, out_dir):
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        getattr(self, self.transform)(*self.params)
        out_path = os.path.join(out_dir,
                                in_path.replace(".wav", f"_{self.transform}.wav"))
        getattr(self, "build")(in_path, out_path)
        arr = self.build_array(in_path)
        assert len(self.effects_log) > 0, "shit happened"


