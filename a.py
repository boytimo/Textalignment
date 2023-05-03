import os

dof_dir = r"C:\Users\boyti\Desktop\Textpy"
log_dir = r"C:\Users\boyti\Desktop\Textpy"
output_dir = r"C:\Users\boyti\Desktop\Textpy"

dof_path = os.path.join(dof_dir, "DOF.txt")
log_path = os.path.join(log_dir, "log.txt")
output_path = os.path.join(output_dir, "merged.txt")

with open(dof_path, "r") as dof_file, open(log_path, "r") as log_file, open(output_path, "w") as merged_file:
    # 머리글 작성
    merged_file.write("index, Row 0, Row 1, Row 2, Row 3, Row 4, Row 5\n")

    dof_lines = dof_file.readlines()
    log_lines = log_file.readlines()

    for index, (dof_line, log_line) in enumerate(zip(dof_lines, log_lines), start=1):
        merged_file.write(f"{index}, {dof_line.strip()}, {log_line.strip()}\n")
