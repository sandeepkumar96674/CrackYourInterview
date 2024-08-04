from collections import deque

# Function to push element x to the front of the deque.
def push_front_pf(dq, x):
    dq.appendleft(x)

# Function to push element x to the back of the deque.
def push_back_pb(dq, x):
    dq.append(x)

# Function to return element from front of the deque.
def front_dq(dq):
    if dq:
        return dq[0]
    return -1

# Function to pop element from back of the deque.
def pop_back_ppb(dq):
    if dq:
        dq.pop()
    return len(dq)

# Driver code to execute the operations based on queries
def process_queries(queries):
    dq = deque()
    results = []
    
    for query in queries:
        if query[0] == 'pf':
            push_front_pf(dq, query[1])
            results.append(query[1])
        elif query[0] == 'pb':
            push_back_pb(dq, query[1])
            results.append(query[1])
        elif query[0] == 'f':
            results.append(front_dq(dq))
        elif query[0] == 'pp_b':
            results.append(pop_back_ppb(dq))
    
    for result in results:
        print(result)