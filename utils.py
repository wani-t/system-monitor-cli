import csv
import time

def save_queue_to_csv(buffer, filename:str):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp', 'cpu', 'memory'])
        writer.writeheader()
        for entry in list(buffer):
            writer.writerow(entry)
    print(f"Data saved to {filename}.")

def get_summary(buffer):
    print("\nLast 5 entries")
    for entry in list(buffer)[-5:]:
        timestamp = time.strftime('%H:%M:%S', time.localtime(entry['timestamp']))
        print(f'{timestamp} | CPU: {entry['cpu']}%, Memory: {entry['memory']}%')
    print()
