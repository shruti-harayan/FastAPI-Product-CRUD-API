from fastapi import APIRouter,HTTPException
from src.utils.utils import get_all_products,create_products
from src.dtos.ProductSchema import CreateProduct,UpdateProduct

productRoutes=APIRouter()

#query param-http://127.0.0.1:8000/product?pro_id=3
@productRoutes.get("/")
def get_all_products_route(pro_id:int=None):
    all_products=get_all_products()
    if pro_id is None:
        return all_products
    for product in all_products:
        if product["id"]==pro_id:
            return product
    raise HTTPException(status_code=404,detail={"Error":"Product not found"})

#path param -http://127.0.0.1:8000/product/2
@productRoutes.get("/{id}")
def get_one_product(id:int):
    all_products=get_all_products()
    for product in all_products:
        if product["id"]==id:
            return product
    raise HTTPException(status_code=404,detail={"Error":"Product not found"})


@productRoutes.post("/")
def create_new_product(product:CreateProduct):
    products=get_all_products()
    product=product.model_dump()
    next_id=max([p["id"] for p in products], default=0)+ 1
    product["id"]=next_id
    products.append(product)
    create_products(products)
    return {
    "message": "Product created successfully",
    "product": product
}


@productRoutes.put("/{id}")
def update_product(id:int,product:UpdateProduct):   
    all_products=get_all_products()
    for idx,p in enumerate(all_products):
        if p["id"] == id:
            changes={}
            for k,v in product.model_dump().items():
                if v is not None:
                    changes[k]=v

            all_products[idx]={"id":id,**p,**changes}
            create_products(all_products)
            return {"message":"product details updated successfully"}
    raise HTTPException(status_code=404,detail="Product not found")


@productRoutes.delete("/{id}")
def delete_product(id:int):
    
    all_products=get_all_products()
    for idx,p in enumerate(all_products):
        if p["id"] == id:
            all_products.pop(idx) #del all_products[idx]
            create_products(all_products)
            return {"message":"product details deleted successfully"}
    raise HTTPException(status_code=404,detail="Product not found")