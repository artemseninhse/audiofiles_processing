## Utility for audiofiles augmentation

This program is a wrapper around Sox library for audio augmentation allowing to apply speed, pad, contrast and dcshift augmentations to one audio or a batch of audios


### Getting started
```
$ git clone https://github.com/artemseninhse/audiofiles_processing.git
$ pip install -r requirements.txt
$ cd audiofiles_processing/
```

### Launch from terminal
```
$ python3 audio_transform.py \
$ --in_path audio_folder \
$ --out_path transformed_folder \
$ --transform pad \
$ --params 1 0
```

### Launch from Jupyter Notebook
```
$ from audio_transform import AudioAug
$ in_path, out_dir = "audio_folder", "transformed_folder"
$ transform, params = "pad", [1, 0]
$ augmentor = AudioAug(transform, params)
$ augmentor.apply(in_path, out_dir)
```

{'cell_type': 'code',
 'execution_count': 1,
 'id': '4e2134b5',
 'metadata': {},
 'outputs': [],
 'source': ['import torch\n',
  'import torch.nn as nn\n',
  'import torch.nn.functional as F\n',
  'import torch.optim as optim\n',
  '\n',
  'from models import SimpleTextCNN\n',
  'from sklearn.model_selection import train_test_split\n',
  'from text_utils import (\n',
  '    TextDataset,\n',
  '    TextTokenizer, \n',
  '    TextProcessor\n',
  ')\n',
  'from torch.utils.data import DataLoader\n',
  'from utils import (\n',
  '    META_PATH, \n',
  '    SEED, \n',
  '    TEST_SIZE,\n',
  '    load_pickle,\n',
  '    dump_pickle,\n',
  '    set_seed\n',
  ')\n']}

