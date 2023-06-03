import pyaudio

def print_available_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')

    print("Available audio devices:")
    for i in range(num_devices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        device_name = device_info.get('name')
        print(f"Device {i}: {device_name}")

    p.terminate()

print_available_devices()
