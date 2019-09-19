import json

input_file = "robot.json"
output_file = "output.txt"


brain = json.load(open(input_file))["brain"]

neurons = brain["neuron"]
connections = brain["connection"]

with open(output_file, "w") as outfile:
    outfile.write("\n")

with open(output_file, "a") as outfile:

    outfile.write("\n")
    for connection in connections:
        src = connection["src"].split("-")
        dest = connection["dest"].split("-")
        weight = connection["weight"]
        res = src[0] + " " + src[1] + " " + dest[0] + " " + dest[1] + " " + str(weight) + "\n"
        #print(res)
        outfile.write(res)

    outfile.write("\n")
    for neuron in neurons:
        if (neuron["type"] == "sigmoid"):
            id = neuron["id"].split("-")
            bias = neuron["bias"]
            res = id[0] + " " + id[1] + " " + str(bias) + "\n"
            #print(res)
            outfile.write(res)
