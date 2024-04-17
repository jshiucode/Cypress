"""
Function to un-jsonify postman output from algorithm run locally
"""
def unjsonify(json):
    output = ""
    print("elapsed time:", json["elapsed_time"])
    i = 0
    lk_count = 0
    for link in json["links"]:
        lk_count += 1
        print(link[0], link[1], link[2])
    print("There were " + str(lk_count) + " links.")

    knot_count = 0
    for knot in json["knots"]:
        knot_count += 1
        print(knot)
    print("There were " + str(knot_count) + " knots.")