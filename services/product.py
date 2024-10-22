from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate

class ProductService:
    
    @staticmethod
    def get_allProduct(db:Session):
        return db.query(Product).all()

    @staticmethod
    def get_product(db: Session, code: str):
        return db.query(Product).filter(Product.code == code).first()

    @staticmethod
    def create_product(db: Session, product: ProductCreate):
        if ProductService.get_product(db, product.code) is not None:
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

    def update_product(db: Session, productid: int, product: ProductCreate):
        db_productid = db.query(Product).filter(Product.id == productid).first()

        db_productid.name = product.name
        db_productid.sale_value = product.sale_value
        db_productid.manages_iva = product.manages_iva
        db_productid.iva_percentage = product.iva_percentage

        db.commit()

        return db_productid

    def deleteProduct(db: Session, productid: int):
        db_productid = db.query(Product).filter(Product.id == productid).first()

        db.delete(db_productid)

        db.commit()

        return db_productid
