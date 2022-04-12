from dataclasses import dataclass

from typing import List


@dataclass
class Configuration:
    binance_key_public: str
    binance_key_private: str
    fav_stocks: List[str]
    fav_leading_index: str
