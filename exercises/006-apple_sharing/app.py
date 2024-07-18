def apple_sharing(n,k):
  # Your code here
  manzanas_por_estudiante = round(k / n) 
  manzanas_en_cesta =  round(k%n) 
  return manzanas_por_estudiante, manzanas_en_cesta
 

print(apple_sharing(6,50))
