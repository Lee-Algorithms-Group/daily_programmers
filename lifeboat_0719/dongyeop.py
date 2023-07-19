from collections import deque

def solution(people, limit):
    count = 0
    people.sort()
    people = deque(people)
    while people:
        p = people.pop()
        count+=1
        if not people: break
        if p+people[0]<=limit:
            people.popleft()
    return count
