
def main():
  import sys
    input_file = sys.argv[1]
  file1 = open(input_file, "r")
  lines = file1.readlines()
  print(len(lines))   
  m = {}
  lines = [int(l) for l in lines] 
  
  mul = {}
  for i, a in enumerate(lines):
    for j, b in enumerate(lines):
       if i == j:
         continue
       mul[a+b] = (i,j)  

  for i, val in enumerate(lines):
    diff = 2020 - val
    if diff in mul:
       if i == mul[diff][0] or i == mul[diff][1]:
         continue
       print(val*lines[mul[diff][0]]*lines[mul[diff][1]])
       break  
 
  


if __name__ == "__main__":
  main()
