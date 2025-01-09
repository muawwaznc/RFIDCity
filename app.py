import pyautogui
import time

def press_down_or_up_key(key, times):
    """Press a specified key (down or up) multiple times."""
    for _ in range(times):
        pyautogui.press(key)
        time.sleep(0.1)  # Add a slight delay between presses

def alt_tab_switch():
    """Perform Alt + Tab to switch windows."""
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(1)  # Give time for the window to switch properly

def main():
    start_time = time.time()  # Record the program's start time
    pressing_down = True  # Start with pressing the Down key
    up_key_time = 2 * 60 * 60  # Switch to Up key after 2 hours
    down_key_time = 4 * 60 * 60  # Switch back to Down key after 4 hours
    
    while True:
        elapsed_time = time.time() - start_time
        
        # Check if it's time to switch to the Up key or revert to the Down key
        if elapsed_time >= up_key_time and elapsed_time < down_key_time:
            pressing_down = False  # Start pressing Up key
        elif elapsed_time >= down_key_time:
            pressing_down = True  # Revert to pressing Down key
            start_time += 4 * 60 * 60  # Reset timer for the next cycle

        # Wait 7 minutes and press keys
        print("Waiting for 7 minutes...")
        time.sleep(7 * 60)

        if pressing_down:
            print("Pressing Down key 32 times...")
            press_down_or_up_key('down', 32)
        else:
            print("Pressing Up key 32 times...")
            press_down_or_up_key('up', 32)
        
        # # Wait another 30 minutes and perform Alt + Tab
        # print("Waiting for 30 minutes before Alt + Tab...")
        # time.sleep(30 * 60)

        # print("Performing Alt + Tab to switch windows...")
        # alt_tab_switch()

        # # Skip pressing keys after Alt + Tab
        # print("Skipping key presses for this cycle...")
        # time.sleep(7 * 60)  # Wait 7 minutes before continuing

        # print("Performing Alt + Tab to switch back to the original window...")
        # alt_tab_switch()

if __name__ == "__main__":
    main()
