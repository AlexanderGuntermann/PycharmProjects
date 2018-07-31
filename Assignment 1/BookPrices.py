discountRate = (25.0 * 0.10) #bookstore discount is 10%

singleBookCost = (25 - discountRate) #cover cost - discount (math is 25 - 2.5 = 22.5)

shippingCostDiscount = 2 * 5 #first 5 books ship for $5 each = 10

remainingShipping = 2.75 * 35 #remaining 35 books ship for 2.75 each = 96.25

totalCost =  (singleBookCost * 40) + shippingCostDiscount + remainingShipping # add cost of book/shipp

print("The total cost of 40 books is: "+ '$'+ str(totalCost)) # prints total cost of 40 books
