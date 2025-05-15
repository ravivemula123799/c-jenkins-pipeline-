import subprocess
import os
import sys

# Detect platform
output_file = "hello.exe" if os.name == "nt" else "hello"

# Compile C code
print("🔧 Compiling hello.c...")
compile = subprocess.run(['gcc', 'hello.c', '-o', output_file], capture_output=True, text=True)

if compile.returncode != 0:
    print("❌ Compilation failed:\n", compile.stderr)
    sys.exit(1)

print("✅ Compilation successful.")

# Run the compiled program
print("▶️ Running the program...")
run = subprocess.run([f"./{output_file}"], capture_output=True, text=True, shell=True)
print("✅ Output:\n", run.stdout)
