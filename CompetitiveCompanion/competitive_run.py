from sys import argv
import os
import subprocess

if __name__ == '__main__':
    folder_path = os.getcwd()

    try:
        subprocess.run(["g++", "-std=c++17", "-Wall", "-o", "solution.exe", "solution.cpp"],
                       check=True)
        print("compilation successful !")
    except:
        print("Compilation failed !")
        exit(0)

    files = os.listdir()
    input_files = [x for x in files if x.strip()[:5] == "input"]
    good = True
    for fname in input_files:
        suffix = fname[5:]
        correct_file = "correct"+suffix
        output_file = "output"+suffix
        error_file = "error"+suffix

        cmd = f"solution.exe <{fname} >{output_file} 2>{error_file}"
        os.system(cmd)

        of = open(output_file, "r")
        outputs = of.read().strip()
        try:
            cf = open(correct_file, "r")
            correct = cf.read().strip()
        except:
            print("Your output : ")
            print("".join(outputs))
            of.close()
            continue

        cf.close()
        of.close()

        if correct != outputs:
            print("\nWA on input file", fname)
            print("\nCorrect output : ")
            print("".join(correct))
            print("Your output : ")
            print("".join(outputs))
            good = False
            print("\nError/Debug Statements:")
            with open(error_file, "r") as f:
                print(f.read())
        else:
            print(fname, "OK !")

    if good:
        print("\n\nAll tests Passed !")
