import collections

class Person(object):
    def __init__(self, name):
        self.name = name

class Solution(object):
    def accountsMerge(self, accounts):
        person2email = collections.defaultdict(list)
        email2person = collections.defaultdict(list)
        for a in accounts:
            p = Person(a[0])
            for e in a[1:]:
                email2person[e].append(p)
                person2email[p].append(e)

        queue = collections.deque()
        visited, results = set(), []
        for e in email2person:
            if e in visited:
                continue
            queue.append(e)
            visited.add(e)
            p_info = [email2person[e][0].name]

            while queue:
                node = queue.popleft()
                p_info.append(node)
                for person in email2person[node]:
                    for new_email in person2email[person]:
                        if new_email in visited:
                            continue
                        queue.append(new_email)
                        visited.add(new_email)
            p_info.sort()
            results.append(p_info)

        return results


test = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]