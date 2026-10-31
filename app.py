
# Sample application for security scanning

import subprocess

# Sample application
username = input("Enter username: ")

if username:
    print("Welcome", username)
else:
    print("Invalid username")

# Run security scanning tools
print("\nRunning Bandit Scan...")
subprocess.run(["bandit", "-r", "."], check=False)

print("\nRunning Dependency Scan...")
subprocess.run(["pip-audit"], check=False)

print("\nSecurity Scan Completed")
