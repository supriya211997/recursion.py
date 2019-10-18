# def test(n):
# 	if n==0:
# 		return 

# 	print("hello")
# 	test(n-1)



# test(5)






# def factorial(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return n*factorial(n-1)


# print(factorial(3))
# print(factorial(5))





# x = [1, 2, 3, 4]
# def addition(array):
#  	if len(array)==0:
#  		return 0
#  	else:
#  		print(array)
#  		return array[0]+(addition(array[1:]))

# print(addition(x))



def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(9)