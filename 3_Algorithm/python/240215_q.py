N = 10
q = [0] * 10
front = rear = -1
rear +=1
q[rear] = 10    # enqueue
rear+=1

q[rear] =20
rear+=1
q[rear] = 30
while front != rear:
    front+=1
    print(q[front])

    