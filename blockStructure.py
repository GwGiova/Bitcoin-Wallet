    #This class defines the structure of a Bitcoin block.
    #[MagicNumber] is a Magic Number which defines the beginning of a block. In the Mainnet it's "f9beb4d9".
    #[Size] is the size of the block, in Bytes.
    #[Version] is the first field inside the block header. It indicates the version count of the Bitcoin Core.
    #[LastBlockHash] contains the hash of the previous block. It make the blockchain unchangeable, making every block interdependent from one another.
    #[MerkleRoot] contains the merkle root. ???
    #[Time] contains the approximate time of the creation of the block. It's inserted by the miner, not calculated by the software.
    #[Target] contains a compressed format to calculate the block target.
    #[Nonce] contains the nonce used to calculate the block hash (that must be < target)
    #[TxNumber] contains the number of transaction contained in the block.
    #[Transactions] !IT'S AN ARRAY! that contains all the transaction in the block.
    class block:

        def __init__(self, MagicNumber, Size, Version, LastBlockHash, MerkleRoot, Time, Target, Nonce, TxNumber, Transactions)

            self.MagicNumber = MagicNumber

            self.Size = Size

            self.Version = Version

            self.LastBlockHash = LastBlockHash

            self.MerkleRoot = MerkleRoot

            self.Time = Time

            self.Target = Target

            self.Nonce = Nonce

            self.TxNumber = TxNumber

            #It's an array
            self.Transactions = Transactions