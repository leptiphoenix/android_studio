import hashlib

class FacialCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class BlockList:
    global listBlock 
    listBlock = []
    def __init__(self):
        return

    def addBlock(self,block):
        listBlock.append(block)
        return
    def lastBlock(self):
        print(len(listBlock))
        if len(listBlock) == 0:
            return "first Contract"
        else:
            return listBlock[-1]

    def lastBLockHash(self):
        print(len(listBlock))
        if len(listBlock) == 0:
            return "first Contract"
        else:
            return listBlock[-1].block_hash 

