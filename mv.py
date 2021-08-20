file = open("mv.txt", "r")
h = file.readlines()
len_h = len(h)
with open('mvreal.txt', 'w') as f:
   for i in range(0, len_h):
      s = h[i]
      if s[0] != '0':
         f.write(s)
         f.write('\n')
         x = 1
      if s[0] == 0:
         x += 1
         if x > 200:
            print("error")
      print(x)