import pandas as pd
from Scrapping import get_data
import datetime
import pathlib
import os

path = pathlib.Path(__file__).parent

def create_df():
    global main_df    
    main_df = pd.DataFrame({"Products":[], "Head":[], "Price":[], "Unit":[], "Price/Unit":[]})
    return(main_df)
    
create_df()

def get_p():
    global main_df
    create_df()   
    temp = pd.read_csv("Product List.csv", index_col=0)
    main_df["Products"] = temp["Products"]
    return(main_df)
        
def save_df():
    date = datetime.datetime.now()
    try:
        os.makedirs(fr"{path}\Backup File")
    except:        
        pass
    backup_file = f"Products {str(date.date())}.csv"
    backup = fr"{path}\Backup File\{backup_file}" 
    try:
        main_df.to_csv(backup, encoding='utf-8')    
        print("Backup saves as " + backup_file)
    except:
        print("Could not saved BACKUP!!!")
        
def save_p():
    main_df["Products"].to_csv(fr"{path}\Product List.csv", encoding='utf-8')    
        
def reset_df():
    global main_df
    if input("Are you sure? ('Yes')") == "Yes":
        try:
            create_df()
            print("Resetted")
            save_p()
        except:
            print("Could not reset!")
    
def add_p():
    global main_df
    product_name = input("Product name? : ")    
    main_df.loc[len(main_df)] = [product_name, None, None, None, None]
    print(product_name + " added to the product list")  
    save_p()

def delete_p():
    global main_df
    product_name = input("Product name? : ")
    if product_name in main_df["Products"].values:
        try:        
            main_df = main_df.drop(main_df[main_df['Products'] == product_name].index)
            save_p()
            print(product_name + " deleted from the product list")  
        except:
            print(f"Could not deleted {product_name} from the list")
    else:
        print("Can't find a product which named :" + product_name)
    return(main_df)
    
def update_df():
    global main_df
    main_df[["Head", "Price", "Unit"]] = main_df["Products"].apply(get_data)
    main_df["Price/Unit"] = main_df.Price / main_df.Unit
    return(main_df)