class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(id={self.student_id}, name={self.name}, age={self.age})"


class StudentQueueArray:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def enqueue(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student instances can be enqueued")
        self.queue.append(student)
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        student = self.queue[self.front]
        self.front += 1
        # Optionally: Remove the front elements to free up space
        if self.front > len(self.queue) // 2:
            self.queue = self.queue[self.front:]
            self.front = 0
            self.rear = len(self.queue)
        return student

    def is_empty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    def __repr__(self):
        return f"StudentQueueArray(queue={self.queue[self.front:self.rear]}, front={self.front}, rear={self.rear})"


# Example usage
if __name__ == "__main__":
    # Create a queue
    queue = StudentQueueArray()

    # Create some students
    student1 = Student(1, "Musrat", 20)
    student2 = Student(2, "Shuvo", 22)
    student3 = Student(3, "Ryam", 21)

    # Enqueue students
    queue.enqueue(student1)
    queue.enqueue(student2)
    queue.enqueue(student3)

    # Display the queue
    print("Queue after enqueuing students:")
    print(queue)

    # Dequeue a student and display it
    removed_student = queue.dequeue()
    print("Dequeued:", removed_student)

    # Display the queue after dequeue
    print("Queue after dequeuing one student:")
    print(queue)
