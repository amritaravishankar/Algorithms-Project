a = [7,6,5,1,2,3,4,5]

if(a[0]<a[len(a)-1]):
  print(a[0])
else:
  #print("here")
  begin = 0
  end = len(a) - 1
  #print(begin, end)
  while(begin<=end):
    mid = ((begin+end) / 2)
    mid = int(mid)
    #print(mid)
    if(a[mid]<a[end]):
      end = mid
    else:
      begin = mid+1
  print(a[mid])
