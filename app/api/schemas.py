from pydantic import BaseModel

class BalanceResponse(BaseModel):
    balance: str

class BalancesResponse(BaseModel):
    balances: list[str]

class TopHoldersResponse(BaseModel):
    holders: list[tuple[str, str, str]]