import sys

# Function to calculate total head movements for FCFS algorithm
def fcfs(head, requests):
    total_head_movements = abs(head - requests[0])
    for i in range(1, len(requests)):
        total_head_movements += abs(requests[i] - requests[i - 1])
    return total_head_movements

# Function to calculate total head movements for SCAN algorithm
def scan(head, requests, num_cylinders):
    requests.sort()
    total_head_movements = 0
    direction = -1  # -1 for moving towards 0, 1 for moving towards max cylinder
    idx = 0

    while idx < len(requests):
        if head == 0:
            direction = 1
        elif head == num_cylinders - 1:
            direction = -1
        
        if (direction == -1 and requests[idx] < head) or (direction == 1 and requests[idx] > head):
            idx += 1
            continue
        
        if direction == -1:
            total_head_movements += head
            head = 0
        else:
            total_head_movements += num_cylinders - 1 - head
            head = num_cylinders - 1
        
        total_head_movements += abs(requests[idx] - head)
        head = requests[idx]
        idx += 1

    return total_head_movements

# Function to calculate total head movements for C-SCAN algorithm
def c_scan(head, requests, num_cylinders):
    requests.sort()
    total_head_movements = 0
    direction = -1  # -1 for moving towards 0, 1 for moving towards max cylinder
    idx = 0

    while idx < len(requests):
        if head == 0:
            direction = 1
        
        if direction == -1:
            total_head_movements += head
            head = 0
        else:
            total_head_movements += num_cylinders - 1 - head
            head = 0
        
        while idx < len(requests) and requests[idx] <= head:
            total_head_movements += abs(requests[idx] - head)
            head = requests[idx]
            idx += 1
        
        if idx < len(requests):
            total_head_movements += abs(requests[idx] - head)
            head = requests[idx]
            idx += 1

    return total_head_movements

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py <initial_head_position> <file_with_requests>")
        sys.exit(1)

    initial_head_position = int(sys.argv[1])
    file_with_requests = sys.argv[2]

    num_cylinders = 5000
    with open(file_with_requests, 'r') as f:
        requests = [int(line.strip()) for line in f]

    # Task 1: Original results
    print("Task 1: Original Results")
    print("FCFS:", fcfs(initial_head_position, requests))
    print("SCAN:", scan(initial_head_position, requests, num_cylinders))
    print("C-SCAN:", c_scan(initial_head_position, requests, num_cylinders))

    # Task 2: Optimized results
    print("\nTask 2: Optimized Results")
    sorted_requests = sorted(requests)
    print("FCFS (Optimized):", fcfs(initial_head_position, sorted_requests))
    print("SCAN (Optimized):", scan(initial_head_position, sorted_requests, num_cylinders))
    print("C-SCAN (Optimized):", c_scan(initial_head_position, sorted_requests, num_cylinders))
