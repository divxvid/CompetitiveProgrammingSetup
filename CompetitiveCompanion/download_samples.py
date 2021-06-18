from flask import Flask, request, json
import os

TEMPLATE_LOCATION = r"D:\CompetitiveProgramming\CompetitiveProgrammingSetup\template.cpp"
app = Flask("Competitive Listener")

@app.route("/", methods=["POST"])
def get_data():
    data = request.get_json()

    folder_name = data["name"].strip().replace(' ', '_')

    #create a folder with "folder_name" if it does not exist
    if not os.path.isdir(folder_name):
        os.system(f"mkdir {folder_name}")

    #copy all the samples into the folder created above.
    #format for input files : input_0.txt, input_1.txt ...
    #format for output files : correct_0.txt, correct_1.txt ...
    for num, test in enumerate(data["tests"]):
        input_file_name = f"input_{num}.txt"
        output_file_name = f"correct_{num}.txt"
        with open(os.path.join(folder_name, input_file_name), "w") as f:
            f.write(test["input"])
        with open(os.path.join(folder_name, output_file_name), "w") as f:
            f.write(test["output"])

    #copy in the template file.
    with open(TEMPLATE_LOCATION, "r") as f:
        with open(f"./{folder_name}/solution.cpp", "w") as wf:
            wf.write(f.read())

    print(f"{folder_name} done !")
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, port=10042)
