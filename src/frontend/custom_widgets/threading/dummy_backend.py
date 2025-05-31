from time import sleep
from tqdm import tqdm
import sys
from io import StringIO

def long_task(progress_callback):
    """Long-running task with progress updates."""
    for i in range(5):
        sleep(1)
        progress_callback(i + 1)  # Emit progress update

def long_task2():
    """Long-running task with progress updates."""
    for i in range(5):
        sleep(1)
        print(f"Step {i + 1} completed.")  # Emit progress update

def edit_cat_photos(progress_callback):
    for i in tqdm(range(10), desc="Editing Photos"):
        sleep(1)
        progress_callback(f"Processing image {i+1}/10...")

def edit_cat_photos2():
    for i in tqdm(range(10), desc="Editing Photos"):
        sleep(1)  # Simulate work
        print(f"Processing image {i+1}/10...")

def with_progress(task):
    def wrapper(progress_callback, *args, **kwargs):
        # Capture the output of the task and call progress_callback
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        task(*args, **kwargs)

        # Emit the captured output
        output = sys.stdout.getvalue()
        progress_callback(output)  # Send progress to the callback

        sys.stdout = old_stdout  # Restore stdout
    return wrapper

# Wrap the task function
# print("does this execute?")     # it does
# wrapped_task = with_progress(edit_cat_photos2)