import  pandas as pd



#Import
orders = pd.read_csv("./2019 Winter Data Science Intern Challenge Data Set.csv")

## Q1
#Test the wrong answer of calculating AOV, the same answer as stated in question
print("The wrong AOV from the question is" ,orders["order_amount"].mean())

#Check ASP(Average Selling Price) for all orders
print("The ASP without data clening is", sum(orders["order_amount"]) / sum(orders["total_items"]))

# Find that the average item value is around 357, there some orders with unusual average item amount,
# A sneaker like this model should not be sold for more than 500
# Some order sold one sneaker for 25725 which are unreasonable
print(" ")
print("The orders with average item mount greater than 500 are listed below")
print(orders[(orders["order_amount"]/orders["total_items"]) > 500][["order_amount","total_items"]])
print(" ")
#Remove orders which sold one sneaker for 25725
orders_without_outliers = orders[(orders["order_amount"]/orders["total_items"]) < 500]

# Find that some orders order much more shoes than others, which are also unusual, they may be sellstore not individual
# Some orders have 2000 items, which are also not reasonable, they are not likelly to be ordered by individual
print(" ")
print("The orders with total items greater than 10 are listed below")
print(orders_without_outliers[orders_without_outliers["total_items"] > 10]["total_items"])
print(" ")

#Remove orders which sold more than 10 sneakers
orders_without_outliers = orders_without_outliers[orders_without_outliers["total_items"] <= 10]

#Lastlly the ASP is 151.7, which is reasonable
print("The final ASP after data cleaning is",
      sum(orders_without_outliers["order_amount"]) / sum(orders_without_outliers["total_items"]))

#The new AOV is 302.6
print("The final AOV after data cleaning  is" ,orders_without_outliers["order_amount"].mean())