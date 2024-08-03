
import subprocess
import time
import argparse

def run_command_in_terminal(command, x_pos, y_pos, title):
    subprocess.Popen(['xterm', '-hold', '-geometry', f'80x20+{x_pos}+{y_pos}', '-fa', 'Monospace', '-fs', '10', '-T', title, '-e', command])
    time.sleep(0.5)  # Adjust the delay as needed

def main(domain):
    # Positioning terminals in four corners of the screen
    screen_width = 1920  # Adjust according to your screen resolution
    screen_height = 1080  # Adjust according to your screen resolution
    margin = 10

    # Top-left corner
    run_command_in_terminal(f"amass enum -d {domain}", margin, margin, f"Amass - {domain}")

    # Top-right corner
    run_command_in_terminal(f"sublist3r -d {domain}", screen_width - 80*10 - margin, margin, f"Sublist3r - {domain}")

    # Bottom-left corner
    run_command_in_terminal(f"nmap -sV {domain}", margin, screen_height - 20*10 - margin, f"Nmap - {domain}")

    # Bottom-right corner
    run_command_in_terminal(f"sqlmap -u http://{domain} --batch", screen_width - 80*10 - margin, screen_height - 20*10 - margin, f"SQLMap - {domain}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run security tools in separate terminal windows.")
    parser.add_argument("domain", help="The domain to run the tools against.")
    args = parser.parse_args()
    main(args.domain)
