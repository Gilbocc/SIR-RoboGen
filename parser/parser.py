import json

input_file = "robot.json"
output_file = "output.json"

brain = json.load(open(input_file))['brain']

neurons = brain["neuron"]
connections = brain["connection"]

with open(output_file, "a") as outfile:

    print("\n")
    for connection in connections:
        src = connection["src"].split("-")
        dest = connection["dest"].split("-")
        weight = connection["weight"]
        res = src[0] + " " + src[1] + " " + dest[0] + " " + dest[1] + " " + str(weight)
        print(res)
        #json.dump(res, outfile)

    print("\n")
    for neuron in neurons:
        if (neuron["type"] == "sigmoid"):
            id = neuron["id"].split("-")
            bias = neuron["bias"]
            res = id[0] + " " + id[1] + " " + str(bias)
            print(res)
            #json.dump(res, outfile)
