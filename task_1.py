from queue import Queue
import time

request_queue = Queue()

request_id = 0


def generate_request():
    global request_id
    request_id += 1

    new_request = {
        "id": request_id,
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    request_queue.put(new_request)
    print(f"Generated request #{new_request['id']} at {new_request['time']}")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing request #{request['id']} created at {request['time']}")
    else:
        print("Queue is empty.")


def main():
    print("System started. Type 'exit' to stop.\n")

    while True:
        generate_request()
        process_request()

        cmd = input("Enter 'exit' to stop or press Enter to continue: ").strip().lower()
        if cmd == "exit":
            print("System stopped.")
            break


if __name__ == "__main__":
    main()
