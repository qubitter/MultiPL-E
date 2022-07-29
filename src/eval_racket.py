# Authored by Arjun Guha
import os
import subprocess
from pathlib import Path

def eval_script(path: Path):
    try: 
        # Assumes exit-code 0 is all okay
        # Run racket on the file, capturing stderr
        output = subprocess.run(" ".join(["racket", str(path)]), shell=True, capture_output=True, timeout=5)
        if output.returncode == 0:
            status = "OK"
        else:
            outmessage = str(output)
            if 'read-syntax' in outmessage:
                status = "SyntaxError"
            else:
                status = "Exception"
        returncode = output.returncode
    except subprocess.TimeoutExpired as exc:
        status = "Timeout"
        output = exc
        returncode = -1
    except subprocess.CalledProcessError as exc:
        status = "Exception"
        returncode = exc.returncode
        output = exc
    return {
            "status": status,
            "exit_code": returncode,
            "stdout": str(output.stdout),
            "stderr": str(output.stderr),
                }



def main():
    directory = Path(Path(__file__).parent, "..", "datasets", "racket-keep-code_davinci_001_temp_0.2-0").resolve()

    for filename in os.listdir(directory):
        r = eval_script(Path.joinpath(directory,filename))
        filename = filename.split(".")[0]
        print(f"Racket,{filename},{r['status']}")

if __name__ == "__main__":
    main()
