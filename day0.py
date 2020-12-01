
def main():
  input_file="/Users/manushree/Downloads/input.txt"
  file1 = open(input_file, "r")
  lines = file1.readlines()
  print(len(lines))   
  m = {}
  for l in lines:
    m[int(l)] = True
  for l in lines:
    i = int(l)
    if 2020-i in m:
       print(i*(2020-i))
       break  

if __name__ == "__main__":
  main()
