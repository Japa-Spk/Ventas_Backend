from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

class ProductService:
    
    @staticmethod
    def create_product(db: Session, product: ProductCreate):
        if ProductService.product_exists(db, product.code):
            raise Exception("El producto ya existe.")

        db_product = Product(**product.dict())
        db.add(db_product)
        try:
            db.commit()
            db.refresh(db_product)
        except Exception as e:
            db.rollback()
            raise Exception("Error al crear el cliente. -> ") from e
        return db_product

    @staticmethod
    def product_exists(db: Session, code: str) -> bool:
        return db.query(Product).filter(Product.code == code).first() is not None