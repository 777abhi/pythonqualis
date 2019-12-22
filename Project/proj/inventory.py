import py

py
class InsufficientException(Exception):
  pass

class MobileInventory:
  balance_inventory = {}
  
  def __init__(self):
    self.inventory = None
    balance_inventory = {}
  
  def __init__(self, inventory,balance_inventory):
    self.inventory = inventory
    self.balance_inventory = self.inventory
    if (isinstance(self.inventory, dict)) == False:
      raise TypeError("Input inventory must be a dictionary")
    for key in self.inventory:
      if (isinstance(key, str)) == False:
        raise ValueError("Mobile model name must be a string")
    for key in self.inventory:
      if (isinstance(self.inventory[key], int)) == True and self.inventory[key] < 0:
        raise ValueError("No. of mobiles must be a positive integer")
  


  def add_stock(self, new_stock):
    if (isinstance(new_stock, dict)) == False:
      raise TypeError("Input inventory must be a dictionary")
    for key in new_stock:
      if (isinstance(key, str)) == False:
        raise ValueError("Mobile model name must be a string")
    for key in new_stock:
      if (isinstance(new_stock[key], int)) == True and new_stock[key] < 0:
        raise ValueError("No. of mobiles must be a positive integer")
    self.balance_inventory.update(new_stock)


  def sell_stock(self,requested_stock):
    if (isinstance(requested_stock, dict)) == False:
      raise TypeError("Input inventory must be a dictionary")
    for key in requested_stock:
      if (isinstance(key, str)) == False:
        raise ValueError("Mobile model name must be a string")
    for key in requested_stock:
      if (isinstance(requested_stock[key], int)) == True and requested_stock[key] < 0:
        raise ValueError("No. of mobiles must be a positive integer")

    for key in requested_stock:
      if key in self.balance_inventory:
        if self.balance_inventory[key]>0:
          self.balance_inventory[key] = self.balance_inventory[key]-requested_stock[key]
        elif self.balance_inventory[key]==0: 
          raise InsufficientException("Insufficient Stock")
      else:
        raise InsufficientException("No Stock. New Model Request")

#c = MobileInventory({'iPhone Model X':2, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25},{})
#print("Original DIct-->")
#print(c.inventory)

#c.add_stock({'iPhone eModel X':100, 'Xiaomi eModel Y': 1000, 'Nokia eModel Z':25})
#print("update Dict-->")
#print(c.balance_inventory)

#c.sell_stock({'iPhone Model X':2})
#print("Stock Removed from Dict-->")
#print(c.balance_inventory)

#c.sell_stock({'kk':2})

