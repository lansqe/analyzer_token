from fastapi import APIRouter, HTTPException
from app.core.blockchain import BlockchainService
from app.api.schemas import BalanceResponse, BalancesResponse, TopHoldersResponse

router = APIRouter()
blockchain = BlockchainService()

@router.get("/balance/{address}", response_model=BalanceResponse)
async def get_balance(address: str):
    try:
        balance = blockchain.get_balance(address)
        return {"balance": str(balance)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/balance/batch", response_model=BalancesResponse)
async def get_balances_batch(addresses: list[str]):
    try:
        balances = blockchain.get_balances(addresses)
        return {"balances": [str(b) for b in balances]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/top_holders/{count}", response_model=TopHoldersResponse)
async def get_top_holders(count: int):
    #          заглушка
    return {"holders": [("0x123...", "1000", "2023-01-01") for _ in range(count)]}

@router.get("/token_info")
async def get_token_info():
    try:
        return blockchain.get_token_info()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))