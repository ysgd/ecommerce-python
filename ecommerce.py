# Requirements
# Ask the user if he/she wants to login or register
# Register - Ask username, password, usertype (Buyer/Seller) and store it in a file
# Login - Ask username and password , if the username and password exists on userdata file then print login successfull. Check the usertype.
# If the user is buyer , give him choices : View all products, View his/her bills, Purchase products. If the user is seller : Add products, View his/her products, View his/her products bills

# User data = {"username":"ram","password":"ram123","usertype":"buyer"}

import json

def register():
      username = input('enter your username: ')
      password = input('create your password: ')
      usertype = input('would you like to register as buyer or seller?: ').lower()
      user_data = {'username': username, 'password': password,      'usertype': usertype}
      json_user_data = json.dumps(user_data)

      f = open('F:/Python/ecommerce/file/userdatas.txt', 'a')

      f.write(json_user_data + '-')
      f.close()

      print('registration successfull')
      after_reg = input('would you like to login? [y/n]: ').lower()
      if after_reg == 'y':
       login()
      elif after_reg == 'n':
       print('thank you for registering')
      else:
       print("please press either 'y' or 'n'")

def login():
    username = input('enter your username: ')
    password = input('enter your password: ')
    f = open('F:/Python/ecommerce/file/userdatas.txt','r')
    json_user_data = f.read()
    f.close()
    list_user_data = json_user_data.split('-')
    user_login = False
    for i in list_user_data:
      if i!='':
        dict_data = json.loads(i)
        if (username == dict_data.get('username') and password ==dict_data.get('password')):
          user_login = True
          type = dict_data.get('usertype')
          break
      
    if user_login == True:
        print('login successfull')
        if type == 'buyer':
          print(f"welcome {dict_data.get('username')} to your buyer account")
          print('what would you like to do?')
          user_operation = input('view products/ purchase/ view bills: ')
          if user_operation == 'view product' or user_operation =='view products':
            view_products(username)
          elif user_operation == 'purchase':
            purchase(username)
          elif user_operation == 'view bills':
            view_bills()
          else:
            print('invalid operation')
          
        else:
          print(f"welcome {dict_data.get('username')} to your seller account")
          print('what would you like to do?')
          user_operation = input('add product/ view product/ view bills: ').lower()
          if user_operation == 'add product' or user_operation =='add products':
            add_product()
          elif user_operation == 'view products' or user_operation== 'view add_product':
            view_products()
          elif user_operation == 'view bills':
            view_bills()
          else:
            print('invalid operation')   
    else:
      print('invalid Credentials')


def view_products(username):
  f = open('F:/Python/ecommerce/file/products.txt','r')
  json_data = f.read()
  f.close()
  list_product_data = json_data.split('-')
  for i in list_product_data:
    print(i)
    
  purchase(username)

def purchase(username):
  purchase_product_name = input('Which product do you want to buy? ')
    
  purchase_quantity = int(input('How much quantity? '))

  f = open('F:/Python/ecommerce/file/products.txt','r')

  product_json_data = f.read()

  f.close()

  list_product_data = product_json_data.split('-')
  stock = False
  product_dict_data = None
  for i in list_product_data:
        if i != '':
            dict_data = json.loads(i)
            if purchase_product_name == dict_data['purchase_product_name']:
                stock = True
                product_dict_data = dict_data
                price = int(dict_data['product_price'])
                break
    

  if stock == True:
        print(f"Purchase of {purchase_product_name} completed!")
        total = purchase_quantity * price
        print(f'Your total is {total}')
        
        bill_data = {'buyer': username, 'product_name': product_dict_data.get(purchase_product_name), 'quantity': purchase_quantity, 'product_price': product_dict_data.get('product_price'), 'total': total}
        json_bill_data = json.dumps(bill_data)
        f = open('F:/Python/ecommerce/file/bill.txt','a')
        f.write(json_bill_data)
        f.close()
  else: 
        print(f"Product with name {purchase_product_name} not available!")
        purchase(username)
        
        purchase_bill = input('would you like to view your bill? [y/n]: ').lower()
        if purchase_bill == 'y':
          view_bills()
        else:
          print('Thank you for purchasing the product')
        
 
        

def view_bills():
  f = open('F:/Python/ecommerce/file/bill.txt','r')
  bill_json_data = f.read()
  f.close()
  bill_json_data = bill_json_data.split('-')
  for i in bill_json_data:
      print(i)

def add_product():
  product_name = input('enter product name: ')
  product_description = input('enter product description: ')
  product_price = input('enter product price: ')
  product_data = {"product_name": product_name, "product_description": product_description, "product_price": product_price}
  json_product_data = json.dumps(product_data)
  f = open('F:/Python/ecommerce/file/products.txt', 'a')
  f.write(json_product_data + '-')
  f.close()
  print('your product has been added')
  

user_choice = input('Would you like to register or login?: ').lower()

if user_choice == 'register':
      register()
elif user_choice == 'login':
      login()
else:
      print('typo mistake')
