def extractMC(location):
    # file open
    # f = open('/Users/hyun/workspace/python_test/test.txt', "r")
    f = open(location, "r")

    # declare valuable
    ARMS_robot = list()
    i=0

    # list based on each lines of file
    for line in f:
        data_list = line.split()

        # find my value 'use' in listed line, returne the value, save
        # i can find the line because (i already know how does it look like)
        # can i found without known of the file?
        try:
            while i<2:
                if data_list.index('use') == 2:
                    # print(data_list)
                    ARMS_robot.append(data_list[4])
                    i=i+1
        except ValueError:
            pass

    # print out the value
    # print(ARMS_robot)

    # close the file
    f.close()

    return ARMS_robot

MC = extractMC('/Users/hyun/workspace/python_test/test.txt')
print(MC)