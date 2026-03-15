from src.app.job.customers.customer_job import customer_job
from src.app.job.products.products_job import product_job 
from src.app.job.purchase.purchase_job import purchase_job
from src.app.job.sales.sales_job import sales_job

def main():
    print("Hello from nga-data-processing-engine!")
    customer_job(path='E:/nga-data-processing-engine/data/customers.csv')
    product_job(path='E:/nga-data-processing-engine/data/products.csv')
    purchase_job(path='E:/nga-data-processing-engine/data/purchase.csv')
    sales_job(path='E:/nga-data-processing-engine/data/sales.csv')
    
if __name__ == "__main__":
    main()

