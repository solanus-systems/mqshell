# ESP32 mocks for Unix

import gc


class Partition:
    @classmethod
    def RUNNING(cls):
        pass

    def __init__(self, _which):
        self.contents = open("partition.bin", "wb")

    def get_next_update(self):
        return self

    def writeblocks(self, _block, buf):
        assert len(buf) == 4096, f"Bad block size: {len(buf)}"
        self.contents.write(buf)
        self.contents.flush()
        gc.collect()

    def set_boot(self):
        self.contents.close()
