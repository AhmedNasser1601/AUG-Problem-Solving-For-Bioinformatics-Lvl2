
def rabbits(n, m):
    generations = [1, 1]
    for cnt in range(2, n+1):

        if cnt < m:  # el w2t ely by3e4oh lesa m5ls4, kol el aranb lesa m3aya, lesa mbd2o4 ymoto
            generations.append(generations[cnt - 2] + generations[cnt - 1])

        elif cnt == m or cnt == m + 1:  # kolhom m3aya ela arnb wa7d 3da 3leh m months 5alas
            generations.append((generations[cnt - 2] + generations[cnt - 1]) - 1)

        else:
            generations.append((generations[cnt - 2] + generations[cnt - 1]) - (generations[cnt - (m + 1)]))

    print(generations)
    return generations[n - 1]


n = int(input('n: '))
m = int(input('m: '))
ans = rabbits(n, m)
print(ans)
