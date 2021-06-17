from sys import argv
import os
import subprocess

if __name__ == '__main__':
    folder_path = os.getcwd()

    if "solution.exe" not in os.listdir():
        try:
            subprocess.run(["g++", "-std=c++17", "-Wall", "-o", "solution.exe", "solution.cpp"],
                           check=True)
            print("compilation successful !")
        except:
            print("Compilation failed !")
            exit(0)
    else:
        print("Using existing Binary. Recompile if needed.\n")

    files = os.listdir()
    input_files = [x for x in files if x[:5] == "input"]
    good = True
    for fname in input_files:
        suffix = fname[5:]
        correct_file = "correct"+suffix
        output_file = "output"+suffix
        cmd = f"solution.exe <{fname} >{output_file}"
        os.system(cmd)
        cf = open(correct_file, "r")
        of = open(output_file, "r")

        correct = cf.read().strip()
        outputs = of.read().strip()

        cf.close()
        of.close()

        if correct != outputs:
            print("\nWA on input file", fname)
            print("\nCorrect output : ")
            print("".join(correct))
            print("Your output : ")
            print("".join(outputs))
            good = False
        else:
            print(fname, "OK !")

    if good:
        print("\n\nAll tests Passed !")
