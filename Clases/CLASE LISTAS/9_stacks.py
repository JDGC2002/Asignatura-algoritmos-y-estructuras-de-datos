# Stacks como listas
s = []
s.append("eat")
s.append("sleep")
s.append("code")
print(s)
input("Press Enter to continue...")

# Extraer último elemento en ingresar
le = s.pop()
print(le)
print(s)
input("Press Enter to continue...")

# extraer más...
s.pop()
s.pop()
print(s)


# Stacks como dequeue (más rápidas y robustas)
from collections import deque
s = deque()
s.append("eat")
s.append("sleep")
s.append("code")
print(s)
input("Press Enter to continue...")

# Extraer último elemento en ingresar
le = s.pop()
print(le)
print(s)
input("Press Enter to continue...")

# extraer más...
s.pop()
s.pop()
print(s)