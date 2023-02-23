from collections import defaultdict


def accountsMerge(accounts):
    G, seen, ans = defaultdict(list), set(), []

    for acc in accounts:
        for i in range(2,len(acc)):
            G[acc[i]].append(acc[i-1])
            G[acc[i-1]].append(acc[i])

    def dfs(email):
        seen.add(email)
        emailList = [email]
        for E in G[email]:
            if E not in seen:
                emailList.extend(dfs(E))
        return emailList
    for acc in accounts:
        if acc[1] not in seen:
            ans.append([acc[0]] + sorted(dfs(acc[1])))
    return ans

accounts = [["David","David5@m.co","David8@m.co"],["David","David1@m.co","David1@m.co","David8@m.co"],["David","David0@m.co","David0@m.co","David5@m.co"]]
print(accountsMerge(accounts))