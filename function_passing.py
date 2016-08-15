
def num_ones_in_binary(x):
  return bin(x).count('1')

def most_ones_in_binary(L):
  L = sorted(L, key=num_ones_in_binary)
  print(L)
  return L[-1]

def num_digits(k):
  return len(str(k))

def most_digits(L):
  L = sorted(L, key=num_digits)
  return L[-1]

def largest_two_digit_even(L):
  two_digit_evens = [i for i in L if num_digits(i) == 2 and i%2 == 0]
  return sorted(two_digit_evens)[-1]

def best(L, criteria):
  return criteria(L) 

def main():
  L = [1, 76, 84, 95, 214, 1023, 511, 32]	
  print(best(L, min))
  print(best(L, largest_two_digit_even))
  print(best(L, most_digits))
  print(best(L, most_ones_in_binary))

if __name__ == '__main__':
	main()