import datetime
import psutil, schedule,time,signal,os
from auto_email import send_email

pid=int(input("Enter the PID of the process you want to monitor: "))
ram=int(input("Enter the ram usage alert threshold in MB: "))
cpu=int(input("Enter the ram usage alert threshold as percentage: "))

def byteMB(val):
    return round(val/(1024**2),2)

def complete_log(pid):
    path = os.path.join(os.getcwd(), f"./complete/{pid}.txt")
    # if the file does not exist, create it, otherwise append to it
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("CPU Stats:\n")
            f.write(f"Percent of CPU Used: {psutil.cpu_percent(interval=1,percpu=True)}\n")
            f.write(f"Number of CPUs: {psutil.cpu_count(logical=False)}\n")
            f.write(f"Clock Frequency of the CPUs: {psutil.cpu_freq(percpu=True)}\n")
            f.write("====================================================\n\n")
            f.write("Memory Stats:\n")
            f.write(f"Memory Usage: {psutil.virtual_memory()}\n")
            f.write("====================================================\n\n")
            f.write("Network Stats:\n")
            f.write(f"{psutil.net_io_counters(pernic=True)}\n")
            f.write("====================================================\n\n")
            f.write("Process Data:\n")
            p=psutil.Process(pid)
            f.write(f"Parent PID: {p.ppid()}\n")
            f.write(f"Process Name: {p.name()}\n")
            f.write(f"Command used for the process:\n{p.cmdline()}\n")
            f.write(f"Environmental Variables:\n{p.environ()}\n")
            f.write(f"Created at: {p.create_time()}\n")
            f.write(f"Open Files:\n{p.open_files()}\n")
            f.write(f"Process Status: {p.status()}\n")
            f.write(f"Current Working Directory: {p.cwd()}\n")
            f.write(f"User who initiated it: {p.username()}\n")
            f.write(f"Terminals associated: {p.terminal()}\n")
            f.write(f"Number of Context Switches: {p.num_ctx_switches()}\n")
            f.write(f"Number of threads used: {p.num_threads()}\n")
            f.write(f"CPU Used: {p.cpu_percent()}\n")
            f.write(f"Memory Info:\n{p.memory_full_info()}\n")
            f.write(f"Existing Memory Maps:\n{p.memory_maps()}\n")
            f.write("====================================================\n\n")

def get_process_data(pid,ram):
    try:
        p=psutil.Process(pid)
        with p.oneshot():
            # For RAM Usage: 
            ram_usage=byteMB(p.memory_info().rss)
            print(f"RSS: {byteMB(p.memory_info().rss)} MB")
            print(f"VMS: {byteMB(p.memory_info().vms)} MB")
            print(f"SHARED: {byteMB(p.memory_info().shared)} MB")
            print(f"TEXT: {byteMB(p.memory_info().text)} MB")
            print(f"DATA: {byteMB(p.memory_info().data)} MB")
            # For CPU Usage:
            p_new= psutil.Process(pid)
            cpu_usage = p_new.cpu_percent(interval=1)/psutil.cpu_count()
            print(f"CPU Used by the PID: {cpu_usage}")
            path = os.path.join(os.getcwd(), f"./logs/{pid}.csv")
            # if the file does not exist, create it, otherwise append to it
            if not os.path.exists(path):
                with open(path, "w") as f:
                    f.write(str(datetime.datetime.now()) + "," + str(cpu_usage) + "," + str(ram_usage) + "\n")
            with open(path, "a") as f:
                f.write(str(datetime.datetime.now()) + "," + str(cpu_usage) + "," + str(ram_usage) + "\n")
            print("========================================")
            if (ram<ram_usage or cpu<cpu_usage):
                print("Overall resource usage greater than allowed")
                complete_log(pid)
                send_email(message=f"Get your process of  PID {pid} in control",pid=pid)
                p.send_signal(signal.SIGKILL)
    except:
        print("Prcess with the given process ID doesnt exists right now")
        exit(0)

schedule.every(1).second.do(get_process_data,pid,ram)


def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Process terminated by User")
        exit(0)