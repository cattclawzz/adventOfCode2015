import hashlib

def mineAdventCoin(md5,no0s):
    dec = 0
    for i in range(99_999_999): #putting a cap on it so i don't kill my pc again
        hashValue = hashlib.md5(f"{md5}{dec}".encode()).hexdigest()
        if hashValue [:no0s] == "0"*no0s:
            break
        else:
            dec += 1
    return dec

secretKey = "ckczppom"
print(f"Part1: {mineAdventCoin(secretKey,5)} \nPart2: {mineAdventCoin(secretKey,6)}")