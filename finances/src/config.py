from dataclasses import dataclass


@dataclass
class Configuration:
    binance_key_public: str
    binance_key_private: str
    fav_stocks: list[str]
    fav_leading_index: str
