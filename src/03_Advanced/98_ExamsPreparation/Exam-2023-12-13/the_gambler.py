def print_matrix(b):
    for row in b:
        print(''.join(map(str,row)))

a=100
n=int(input())
gp = []
m=[]
for r in range(n):
    l=list(input())
    m.append(l)
    if "G" in l:
        gp = [r,l.index("G")]
        m[r][gp[1]] = "-"
ms = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right":  (0, 1)
}

while True:
    cmd = input()
    if cmd == "end":
        m[gp[0]][gp[1]] = "G"
        print(f"End of the game. Total amount: {a}$")
        print_matrix(m)
        break

    r, c = ms[cmd]
    nr = gp[0] + r
    nc = gp[1] + c
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        m[gp[0]][gp[1]] = "G"
        print("Game over! You lost everything!")
        break

    if m[nr][nc] == "-":
        gp = [nr, nc]
    elif m[nr][nc] == "W":
        m[nr][nc] = "-"
        a += 100
        gp = [nr, nc]
    elif m[nr][nc] == "P":
        m[nr][nc] = "-"
        gp = [nr, nc]
        a -= 200
        if a <= 0:
            m[nr][nc] = "G"
            print("Game over! You lost everything!")
            break
    elif m[nr][nc] == "J":
        m[nr][nc] = "G"
        gp = [nr, nc]
        a+=100000
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {a}$")
        print_matrix(m)
        break
