# Write your test here


from challenge01 import MyQueue


def test_my_queue():
    # Initialize the queue
    myQueue = MyQueue()

    # Push elements onto the queue
    myQueue.push(1) # queue is: [1]
    myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)

    # Test the peek and pop operations
    assert myQueue.peek() == 1
    assert myQueue.pop() == 1
    assert not myQueue.empty()

    # Push more elements onto the queue
    myQueue.push(3) # queue is: [2, 3]
    myQueue.push(4) # queue is: [2, 3, 4]

    # Test the peek and pop operations again
    assert myQueue.peek() == 2
    assert myQueue.pop() == 2
    assert not myQueue.empty()

    # Pop all remaining elements from the queue
    assert myQueue.pop() == 3
    assert myQueue.pop() == 4
    assert myQueue.empty()

    print("All tests pass.")

test_my_queue()
