from monitor import Monitor
from utils import save_queue_to_csv, get_summary
from live_plot import plot_live
from collections import deque

def main():
    log_buffer = deque(maxlen=1000)
    monitor = Monitor(log_buffer)

    exit = False

    try:
        while not exit:
            cmd = input("Command (start/stop/summary/save/plot/quit): ").strip().lower()

            match cmd:
                case "start":
                    monitor.start()
                case "stop":
                    monitor.stop()
                case "summary":
                    get_summary(log_buffer)
                case "save":
                    save_queue_to_csv(log_buffer, 'system_monitor_logs.csv')
                case "plot":
                    plot_live(log_buffer)
                case "quit":
                    monitor.stop()
                    print("Exiting...")
                    exit = True
                case _:
                    print("Invalid option. Please try again.")

    except KeyboardInterrupt:
        print("Ctrl + C detected. Cleaning up...")
        monitor.stop()
        cnf = input("Save log before quiting? Y/N ").strip().upper()
        if cnf=="Y":
            save_queue_to_csv(log_buffer, 'system_monitor_logs.csv')
            print("Exiting...")
            exit = True
        if cnf=="N":
            print("Exiting without saving log...")
            exit = True


if __name__=="__main__":
    main()
                