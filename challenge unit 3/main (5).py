







def LinearSearchProduct(ProductList,targetProduct):
  indices = []
  
  for index,product in enumerate(ProductList):
    if product == targetProduct:
      indices.append(index)
      
  return indices 



product =["shoes","boot","loafer","shoes","sadal","shoes"]
target = "shoes"
target2 = "apple"
result = LinearSearchProduct(product, target)
print (result)
