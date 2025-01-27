
import subprocess
import sys

def install():
    """Install the package"""
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "allpurpose_gpt"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])

def run():
    """Run the application"""
    subprocess.check_call([sys.executable, "-m", "chainlit", "run", "interface/main.py"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py [install|run]")
        sys.exit(1)
        
    command = sys.argv[1]
    if command == "install":
        install()
    elif command == "run":
        run()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
