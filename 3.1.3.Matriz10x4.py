
bus = [[0 for _ in range(4)] for _ in range(10)]

asiento_num = 1
for i in range(10):
    for j in range(4):
        bus[i][j] = asiento_num
        asiento_num += 1

print("Asientos del bus:")
for fila in bus:
    for asiento in fila:
        print(f"{asiento:2}", end=" ")
    print()
