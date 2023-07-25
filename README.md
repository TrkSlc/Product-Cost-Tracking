This project helps you to keep cost records of the products. 
You make a list of the products you want with python and it takes information from the least priced version of that product that listed in ["cimri.com"](cimri.com.) via web scrapping. Gives you a csv result of the informations about the products listed.

I personaly use it to keep track of raw materials that I use in my candle business. It can be modified to keep any necessary information about a product.

  ```create_df()``` - creates the necessary dataframe(df)
  
  ```add_p()``` - opens an input to add a product to the df

  ```delete_p()``` - opens an input to delete a product from the df
  
  ```save_df()``` - saves the df's backup named with the current date

  ```save_p()``` -  saves the list of products to be able to read when rerunning
  
  ```get_df()``` - reads products list to the df
  
  ```reset_df()``` - resets the df and the saved list of products
  
  ```update_df()``` - runs scrapping functions for the df columns and updates the information about the product

  
