from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import ProductSchemas, ProductModel
from settings import app, get_db

router = APIRouter()

@router.post("/product/", response_model=ProductSchemas)
def create_product(product: ProductSchemas, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products/", response_model=list[ProductSchemas])
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products

@router.get("/products/{product_id}", response_model=ProductSchemas)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product

@router.put("/products/{product_id}", response_model=ProductSchemas)
def update_product(product_id: int, product: ProductSchemas, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for field, value in product.dict().items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/products/{product_id}", status_code=204)
def delete_item(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
