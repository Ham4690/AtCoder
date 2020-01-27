
def magicEnergy(H,A):

H, N = map(int, input().split())
magics = []
for i in range(N):
    magic = list(map(int, input().split()))
    magic.append(magic[0]/magic[1])
    magics.append(magic)

magics.sort(reverse=True, key=lambda x:x[2])

