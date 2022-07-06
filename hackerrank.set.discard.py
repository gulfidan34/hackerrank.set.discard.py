n = int(input())
s = set(map(int, input().split()))
g = int(input())

for x in range(g):
  cmd = input().split()
  if cmd[0] == "remove":
    s.remove(int(cmd[1]))
  elif cmd[0] == "discard":
    s.discard(int(cmd[1]))
  else:
    s.pop()
    
print(sum(s))
