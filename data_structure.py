from __future__ import annotations
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List

@dataclass 
class Transaction:
    merchant: str
    amount: int
    time: datetime

    def __str__(self) -> str:
        return f"Txn({self.amount} @ {self.merchant} on {self.time.isoformat(timespec='seconds')})"
    
    def to_dict(self) -> dict:
        dct = asdict(self)
        dct["time"] = self.time.isoformat()
        return dct
    

@dataclass
class Account:
    active: bool
    available_limit: int
    history: List[Transaction] = field(default_factory=list)

    def can_spend(self, amount: int) -> bool:
        return self.active and amount <= self.available_limit
    
    def register(self, txn: Transaction) -> None:
        if not self.can_spend(txn.amount):
            raise ValueError("Insufficient limit or account inactive")
        self.available_limit -= txn.amount
        self.history.append(txn)

    def __str__(self) -> str:
        return (
            f"Account(active={self.active}, limit={self.available_limit}, "
            f"txn={len(self.history)})"
        )
