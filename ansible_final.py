import subprocess

def showrun():
    command = ['ansible-playbook', 'playbook.yaml']
    result = subprocess.run(command, capture_output=True, text=True)
    print("=== Ansible stdout ===")
    print(result.stdout)
    print("=== Ansible stderr ===")
    print(result.stderr)
    
    if result.returncode != 0:
        return f"Error: Ansible failed with code {result.returncode}"

    if 'ok=2' in result.stdout or 'ok=1' in result.stdout:
        return 'show_run_66070119_R1-Exam.txt'
    else:
        return 'Error: Ansible output unexpected'