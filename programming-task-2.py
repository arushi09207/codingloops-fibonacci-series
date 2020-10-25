#input list elements
li = list(map(int,input().split(" ")))
reqd_li = [] #output positives list
for i in range(len(li)):
  if li[i] < 0:
      pass
  else:
      reqd_li.append(li[i])
print(reqd_li)      
