import queue

request_queue = queue.Queue()

def enqueue_request(data):
    request_queue.put(data)

def dequeue_request():
    return request_queue.get() 