from web3 import Web3
from web3.middleware import geth_poa_middleware
from config import settings

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function"
    }
]


class BlockchainService:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(settings.POLYGON_RPC_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.token_contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(settings.TOKEN_ADDRESS),
            abi=ERC20_ABI
        )

    def get_balance(self, address: str) -> int:
        """Получить баланс адреса в wei"""
        address = Web3.to_checksum_address(address)
        return self.token_contract.functions.balanceOf(address).call()

    def get_balances(self, addresses: list[str]) -> list[int]:
        """Получить балансы нескольких адресов"""
        return [self.get_balance(addr) for addr in addresses]

    def get_token_info(self) -> dict:
        """Получить информацию о токене"""
        return {
            "name": self.token_contract.functions.name().call(),
            "symbol": self.token_contract.functions.symbol().call(),
            "decimals": self.token_contract.functions.decimals().call(),
            "totalSupply": self.token_contract.functions.totalSupply().call()
        }

    def get_last_transaction_date(self, address: str) -> str:
        """Получить дату последней транзакции для адреса (упрощенная версия)"""
        return "2023-01-01"  # заглушка