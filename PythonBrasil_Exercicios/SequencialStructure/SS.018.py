file_download = int(input("What's the file size in MB?"))
net_speed = int(input("Whats the internet speed in MBps?"))
down_sec = file_download / net_speed
down_min = down_sec / 60

print(f'The download time in minutes is: {down_min}')
