import numpy as np
import os

from audio_converter import (
    get_audio_paths,
    convert_mp3_to_wav
)
from os.path import join
from testcases import (
    TEST_DIR_RAW,
    TEST_LIST_AUDIO,
    TEST_MP3
)
from utils import (
    CONVERTED_DIR,
    clear_dir,
    read_wav
)


def run_test(tests_set, test):
    try:
        getattr(tests_set, test)()
        print(f"{test} is executed successfully")
    except AssertionError:
        raise Exception(f"{test} ended with error")


def run_tests():
    tests_set = TestsUnit()
    for test in dir(tests_set):
        if not test.endswith("__"):
            run_test(tests_set, test)


def assert_not_error(func):
    def wrapper(*args):
        try:
            func(*args)
        except:
            raise AssertionError(f"Error during execution of {func.__name__}")
    return wrapper


class TestsUnit:
    def test_get_audios(self):
        assert np.intersect1d(get_audio_paths(TEST_DIR_RAW,
                                              TEST_MP3),
                              TEST_LIST_AUDIO
                              ).shape[0] == 3, "Search of MP3 failed"

    def test_convert_mp3(self):
        dir_convert = join(TEST_DIR_RAW,
                           CONVERTED_DIR)
        clear_dir(dir_convert)
        assert not os.listdir(dir_convert), "Dir not empty"
        convert_mp3_to_wav(TEST_DIR_RAW,
                           TEST_LIST_AUDIO[0]
                           )
        assert TEST_LIST_AUDIO[0].replace("mp3", "wav") in \
               os.listdir(dir_convert), "MP3 conversion failed"

    @assert_not_error
    def test_open_wav(self):
        dir_convert = join(TEST_DIR_RAW,
                           CONVERTED_DIR)
        assert os.listdir(dir_convert), "Empty dir"
        test_wav = join(dir_convert,
                        os.listdir(dir_convert)[0])
        read_wav(test_wav)
        clear_dir(dir_convert)


run_tests()
