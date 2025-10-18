import subprocess

def showrun(student_id, router_name):
    command = ['ansible-playbook', 'C:/Users/LAB306_XX/Documents/GitHub/IPA2024-Final/playbook.yaml']
    result = subprocess.run(command, capture_output=True, text=True)
    
    
    print("Standard Output:\n", result.stdout)
    print("Standard Error:\n", result.stderr)
    
    
    if result.returncode == 0:  # Ansible success returns 0
        return f'show_run_{student_id}_{router_name}.txt'
    else:
        return 'Error: Ansible'

student_id = '66070119'
router_name = 'R1-Exam'
output_file = showrun(student_id, router_name)
print(output_file)