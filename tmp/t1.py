from collections import deque

if __name__ == '__main__':
    q = deque([1,2,3,4,5])
    q.append(6)
    q.appendleft(7)
    print(q)
    q.popleft()
    print(q)
    q.rotate(3)
    print(q)