def which_row(n):
  if n == 1:
    rownumber = 1
    print(f"jeg sidder i række {n} ")
  else:
    print("Hvilken række sidder du i?")
    rownumber = 1+ which_row(n-1)
    print(f"jeg sidder i række {n}")
  return rownumber

which_row(9)