import webbrowser
import os
import time
import subprocess

FASTAPI_DIR='./api'
DASHBOARD_FILE='./dashboard/app.py'
SIMULATOR_FILE = './simulator/simulator.py'

#1.Start the fastapi first
print("Starting the fastapi backend...")
fastapi_process = subprocess.Popen(
    ['uvicorn', 'main:app', '--reload'],
    cwd=FASTAPI_DIR
)
time.sleep(3)

print("Opening Streamlit Dashboard...")
dashboard_process = subprocess.Popen(
    ['streamlit', 'run', DASHBOARD_FILE]
)
# webbrowser.open(f"http://localhost:8501")


print("Opening Streamlit Simulator...")
simulator_process =subprocess.Popen(
    ['python', SIMULATOR_FILE]
)
time.sleep(2)

print("All the services are running. Please press Ctrl+C to stop.")


try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\n Shutting Down")
    fastapi_process.terminate()
    simulator_process.terminate()
    dashboard_process.terminate()