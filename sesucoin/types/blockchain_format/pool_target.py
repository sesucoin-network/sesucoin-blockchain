from dataclasses import dataclass

from sesucoin.types.blockchain_format.sized_bytes import bytes32
from sesucoin.util.ints import uint32
from sesucoin.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class PoolTarget(Streamable):
    puzzle_hash: bytes32
    max_height: uint32  # A max height of 0 means it is valid forever
