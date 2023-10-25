#!/usr/bin/env python3

# Created By: Red+d Forfieda

# Date: October 23, 2023

# This file holds Labour, Rental, Ingredients.
def main():
  #get diameter from user
  diameter = float(input("enter diameter(mm): "))
  #calculate subtotal

  total = 2 + 2.25 + diameter * 1.50 
  subtotal = total * 1.13
#display subtotal
  print("")
  print("subtotal = {} mm^2".format (subtotal))

if __name__ == "__main__":
    main()