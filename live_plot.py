import matplotlib.pyplot as plt
import matplotlib.animation as animation #to animate the live graph
import time

def plot_live(buffer):
    cpu_data=[]
    mem_data=[]
    time_data=[]

    def animate(i): #i is the frame number, starting at 0
        recent_entries = list(buffer)[-20:]
        time_data.clear()
        cpu_data.clear()
        mem_data.clear()

        for entry in recent_entries:
            time_data.append(time.strftime('%H:%M:%S', time.localtime(entry['timestamp'])))
            cpu_data.append(entry['cpu'])
            mem_data.append(entry['memory'])

        plt.cla()
        plt.plot(time_data, cpu_data, label="CPU %")
        plt.plot(time_data, mem_data, label="Memory %")
        plt.xticks(rotation=90, ha='right')
        plt.legend(loc='upper right')
        plt.ylabel('% Usage')
        plt.xlabel('Timestamp')
        plt.title('Live System Monitor')
        plt.tight_layout()

    ani =  animation.FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False) 
    #makes the live graph work by calling animate function repeatedly
    #caching not required for live graph
    #need to save in ani object to avoid it being garbage collected
    plt.show()
