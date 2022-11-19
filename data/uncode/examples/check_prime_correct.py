def check_prime(n):
  if n==1:
    return 0
  j = 2
  while j<n:
    if n%j == 0:
      return 0
    j = j+1 
  return 1
