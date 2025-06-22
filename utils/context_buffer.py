from collections import deque

buffer = deque(maxlen=8)

def update_context(new_text):
    buffer.append(new_text)
    return list(buffer)
