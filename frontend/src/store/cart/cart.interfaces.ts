import { IProduct } from '@/store/products/products.interfaces';

export interface IBasket {
  id: number,
  quantity: string,
  product_id: IProduct,
}

export interface ICart {
  basket: IBasket[],
  total_price: string,
}
