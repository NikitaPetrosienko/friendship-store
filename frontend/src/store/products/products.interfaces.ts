export interface IProduct {
  id: number,
  product_name: string,
  model: string,
  price: string,
  availability: boolean,
  description: string,
  quantity: number,
  main_image: string,
  size: string,
  category: number,
  brand: number
}

export interface IProductComment {
  id: number,
  name_user: string,
  body: string,
  created_at: string,
  product_id: number
}

export interface IProductPage {
  product: IProduct,
  review: IProductComment[],
  images: [],
}
