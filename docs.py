import psutil, schedule, time
def cpu_data():
    # CPU Percentage
    print(psutil.cpu_percent(interval=1,percpu=True))
    # Number of CPU
    print(psutil.cpu_count(logical=False))
    # Clock frequency
    print(psutil.cpu_freq(percpu=True))

def mem_data():
    # Get the existing data about memory
    print(psutil.virtual_memory())
    # Get infor about swap_memory (mainly for linux system)
    print(psutil.swap_memory())

def disk_data():
    # Complete existing disk & its usage
    print(psutil.disk_usage("/"))
    # Check disk partitions
    print(psutil.disk_partitions())

def network_data():
    # Data transfer in each network interface
    print(psutil.net_io_counters(pernic=True))
    # Data transfer in each network protocol
    print(psutil.net_connections(kind="inet"))
    # Address of each interface
    print(psutil.net_if_addrs())

def temp_fans():
    # CPU temp
    print(psutil.sensors_temperatures(fahrenheit=False))
    # Fans
    print(psutil.sensors_fans())
    # Battery percentage
    def secs2hours(secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)
    battery=psutil.sensors_battery()
    print(print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft))))

def process_data():
    # print(psutil.pids())
    # pid=int(input("Enter process id"))
    pid=3471
    p = psutil.Process(pid)
    with p.oneshot():
        # Returns the parent process of the given PID
        print(p.ppid())
        # Returns the name of the process
        print(p.name())
        # CMD used by it
        print(p.cmdline())
        # ENV variable
        print(p.environ())
        # Created time returned as seconds
        print(p.create_time())
        # Returns open files
        print(p.open_files())
        # Current process status
        print(p.status())
        # Current working directory
        print(p.cwd())
        # Username of the user who executed it
        print(p.username())
        # Terminal used by the process
        print(p.terminal())
        # Number of context switches
        print(p.num_ctx_switches())
        # Number of file descriptor used by the process
        print(p.num_fds())
        # Number of threads used by the process
        print(p.num_threads())
        # CPU usage percent
        print(p.cpu_percent())
        # Memory info about the process
        print(p.memory_full_info())
        # Memory usage percent
        print(p.memory_percent())
        # Show memory maps existing
        print(p.memory_maps())


# Schedule take to execute every given interval 
schedule.every(1).seconds.do(process_data)
while True:
    schedule.run_all()
    time.sleep(1)