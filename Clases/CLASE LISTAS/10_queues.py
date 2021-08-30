from collections import deque
s = deque()
s.append("eat")
s.append("sleep")
s.append("code")
print(s)
input("Press Enter to continue...")

# Extraer primer elemento que ingresó
le = s.popleft()
print(le)
print(s)
input("Press Enter to continue...")

# extraer más...
s.popleft()
s.popleft()
print(s)