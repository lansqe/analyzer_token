from datetime import datetime
from sqlalchemy import Column, String, Numeric, DateTime
from app.core.database import Base


class TokenHolder(Base):
    __tablename__ = "token_holders"

    address = Column(String(42), primary_key=True)
    balance = Column(Numeric(78, 0))
    last_transaction_date = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<TokenHolder(address={self.address}, balance={self.balance})>"