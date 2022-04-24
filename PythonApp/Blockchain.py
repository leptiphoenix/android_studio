import hashlib

class FacialCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class BlockList:
    global listBlock, dbConsent, lines
    listBlock = [] 
    dbConsent = open("dataBaseConsentList.txt", "r")
    lines = dbConsent.readlines()

    def __init__(self):
        return

    def addDatabase(self,consent):
        dbAddConsent = open("dataBaseConsentList.txt", "a")
        #IdConsentement /  OUI-non consent / Nom / Prenom / Demeurant / Société ou entité / Date / Lieux
        dbAddConsent.write("[" + str((len(lines)+1)) + "," + str(consent[0])+ "," + str(consent[1])+ "," + str(consent[2])+ "," + consent[3]+ "," + consent[4]+ "," + consent[5]+ "," + consent[6] + "]\n" )
        dbAddConsent.close()
        return

    def addBlock(self,block, consent):
        listBlock.append([len(listBlock),block])
        self.addDatabase(consent)
        f = open("BlockChain", "w")
        for i in listBlock:
            f.writelines(str(i[0]) + str(i[1].block_data))
        return

    def getID(self):
        return len(listBlock)

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

