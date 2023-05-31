export interface ICategory {
  id: number,
  category_name: string
}

export interface IBrand {
  id: number,
  brand_name: string,
  image: string,
}

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
  category: ICategory,
  brand: IBrand
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

export interface IFavouriteProduct {
  id: number,
  user_id: string,
  product_id: IProduct,
}

export interface IFavouriteProduct {
  id: number,
  user_id: string,
  product_id: IProduct,
}
