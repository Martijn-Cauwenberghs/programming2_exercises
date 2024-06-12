# Enter your code here:
class StorageDevice:
    def __init__(self, block_count, block_size):
        self.block_count = block_count
        self.__block_size = block_size
        self.__available_blocks = {i for i in range(0, self.block_count)}
        self.__used_blocks = set()

    @property
    def available_blocks_count(self):
        return self.__available_blocks 

    @property
    def used_block_count(self):
        return self.__used_blocks

    @property
    def total_block_count(self):
        return self.block_count

    @property
    def block_size(self):
        return self.__block_size

    def allocate(self, block_count: int): #takes block_count from available_blocks and returns them as list. Also moves these blocks from available_blocks to used_blocks.
        if (block_count > len(self.available_blocks_count)):
            raise RuntimeError("insufficient blocks left")
        else: 
            start = min(self.__available_blocks)
            removal = {i for i in range(start, start + block_count)}
            self.__available_blocks-= removal
            self.__used_blocks = self.__used_blocks | removal
            return removal

    def free(self, )










test = StorageDevice(32, 16)
print(test.available_blocks_count)
test.allocate(3)
print(test.available_blocks_count)
print(test.used_block_count)
test.allocate(3)
print(test.available_blocks_count)
print(test.used_block_count)