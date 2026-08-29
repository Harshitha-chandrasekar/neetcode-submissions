class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ans = []
        graph = defaultdict(set)
        email_to_name = {}

        for acc in accounts:
            name = acc[0]
            email1 = acc[1]
            for i in range(1,len(acc)):
                email2 = acc[i]
                graph[email1].add(email2)
                graph[email2].add(email1)
                email_to_name[email2] = name

        visited = set()
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                comp = []

                while stack:
                    node = stack.pop()
                    comp.append(node)

                    for newn in graph[node]:
                        if newn not in visited:
                            visited.add(newn)
                            stack.append(newn)
                ans.append([email_to_name[email]] + sorted(comp))

        return ans

