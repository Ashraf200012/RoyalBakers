import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If already refactored, skip
    if 'os.environ.get("DB_HOST"' in content:
        return

    # Check if we need to add import os
    needs_os = 'import os' not in content and 'import mysql.connector' in content

    if needs_os:
        content = re.sub(r'(import mysql\.connector)', r'import os\n\1', content)

    # Replace host
    content = re.sub(r'host\s*=\s*["\']localhost["\']', r'host=os.environ.get("DB_HOST", "localhost")', content)
    # Replace user
    content = re.sub(r'user\s*=\s*["\']root["\']', r'user=os.environ.get("DB_USER", "root")', content)
    # Replace password
    content = re.sub(r'password\s*=\s*["\']["\']', r'password=os.environ.get("DB_PASSWORD", "")', content)
    # Replace database
    content = re.sub(r'database\s*=\s*["\']royalbakers["\']', r'database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306))', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Refactored {filepath}")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.py') and file != 'refactor_db.py' and file != 'server.py':
            process_file(os.path.join(root, file))

print("Done refactoring DB connections!")
