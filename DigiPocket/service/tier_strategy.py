from models.user import Tier

class BaseStrategy:
    def get_limit(self) -> float:
        raise NotImplementedError

class BasicStrategy(BaseStrategy):
    def get_limit(self) -> float:
        return 1_00_000.0

class PremiumStrategy(BaseStrategy):
    def get_limit(self) -> float:
        return 10_00_000.0

class TierFactory:
    _map = {Tier.BASIC: BasicStrategy, Tier.PREMIUM: PremiumStrategy}

    @staticmethod
    def get_strategy(tier: Tier) -> BaseStrategy:
        return TierFactory._map[tier]()