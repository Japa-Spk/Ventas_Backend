import math

from sqlalchemy.orm import Session

from models.sale_header import SaleHeader
from models.sale_detail import SaleDetail
from models.product import Product

from schemas.sale import SaleCreate

from services.user import UserService
from services.product import ProductService

class SaleService:
    
    @staticmethod
    def create_sale(db: Session, sale: SaleCreate):
        print("Crear reg venta")
        errors = SaleService.validate_sale(db, sale)
        if errors:
            list_errors = "\n".join([f"Error:{item}" for item in errors])
            print("list_errors",list_errors)
            raise Exception(f"Error de registro de ventas:\n {list_errors}")
        db_sale_header = SaleHeader(**sale.header.dict())
        db.add(db_sale_header)
        # deferred commit, gets id available without confirming the transaction
        db.flush()
        db_sale_header.consecutive = f"FE-{db_sale_header.id}"
        details_add = []
        for detail in sale.detail:
            db_sale_detail = SaleDetail(**detail.dict())
            db_sale_detail.sale_header_id = db_sale_header.id
            db.add(db_sale_detail)
            details_add.append(db_sale_detail)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise Exception("Error al crear registro de ventas. -> ") from e
        return { "header":db_sale_header, "detail":details_add }

    @staticmethod
    def validate_sale(db:Session, sale: SaleCreate):
        sale_header = SaleHeader(**sale.header.dict())
        errors = []
        if UserService.get_user_id(db, sale_header.user_id) is None:
            errors.append("El cliente no existe, verifique el reigstro de ventas")
        #Valid total_sale
        total_sale_value = 0
        for detail in sale.detail:
            sale_detail = SaleDetail(**detail.dict())
            product: Product = ProductService.get_product_id(db, sale_detail.product_id)
            print("Product -> ", product.code)
            if product.manages_iva:
                total_sale_value += product.sale_value + (product.sale_value * product.iva_percentage)
            else:
                total_sale_value += product.sale_value
        print("total sale value calculation -> ", total_sale_value, "value total sale ->", sale_header.total_sale, "")
        if not math.isclose(total_sale_value,sale_header.total_sale, rel_tol=1e-9, abs_tol=0.0):
            errors.append("El valor del registro de ventas esta mal calculado, verificar")
        
        return errors
                



    