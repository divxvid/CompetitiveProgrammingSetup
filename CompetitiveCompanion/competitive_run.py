from sys import argv
import os
import subprocess

run_op = open("run_info.txt", "w")

def print_(*args):
    print(" ".join(args))
    run_op.write("".join(map(str, args))+"\n")

if __name__ == '__main__':
    folder_path = os.getcwd()

    try:
        subprocess.run(["g++", "-std=c++17", "-Wall", "-o", "solution.exe", "solution.cpp"],
                       check=True)
        print_("compilation successful !")
    except:
        print_("Compilation failed !")
        run_op.close()
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
        outputs = of.read().strip().split()
        try:
            cf = open(correct_file, "r")
            correct = cf.read().strip().split()
        except:
            print_("Your output : ")
            print_("".join(outputs))
            of.close()
            continue

        cf.close()
        of.close()

        if correct != outputs:
            print_("\nWA on input file", fname)
            print_("Input given : ")
            with open(fname, "r") as f:
                print_(f.read())
            print_("\nCorrect output : ")
            print_("".join(correct))
            print_("Your output : ")
            print_("".join(outputs))
            good = False
            print_("\nError/Debug Statements:")
            with open(error_file, "r") as f:
                print_(f.read())
        else:
            print_(fname, "OK !")

    if good:
        print_("\n\nAll tests Passed !")
    run_op.close()
