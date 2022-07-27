# Authored by Arjun Guha
# Copyright (c) 2022, Roblox Inc.
#
# This script runs the Luafied HumanEval programs in datasets/lua
import os
import subprocess
from pathlib import Path

def main():
    directory = Path(Path(__file__).parent, "..", "datasets", "cpp").resolve()
    binary_dir = os.path.join(directory, 'binary')

    for filename in os.listdir(directory):
        if "151_double_the_difference" in filename or '103' in filename or \
        "_39_" in filename or "_125_" in filename or "_137_" in filename or \
        '_95_' in filename or '_22_' in filename or '_130_' in filename or '_133_' in filename or '_51_' in filename:
          continue
        
        if '.cpp' not in filename:
          #Do not compile a binary
          continue
        #TODO: All binaries should go in separate directory
        filepath = os.path.join(directory, filename)
        binary = filepath.replace('.cpp','')
        if os.path.basename(binary) in os.listdir(directory):
          continue
        command = " ".join(["g++", filepath, "-o", binary])
        print(command)
        # Assumes exit-code 0 is all okay
        (code, output) = subprocess.getstatusoutput(command)
        if code == 0:
          status = "OK"
        else:
          status = "SyntaxError"
          print(output)
          return
        # except subprocess.TimeoutExpired as exc:
        #     status = "Timeout"
        filename = filename.split(".")[0]
        print(f"C++,{filename},{status}")

if __name__ == "__main__":
    main()
