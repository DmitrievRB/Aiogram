from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict

from database.models import Product


async def orm_add_product(session:AsyncSession,data:Dict):
    
    obj = Product(
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        image=data['image'],
    )
    session.add(obj)
    await session.commit()