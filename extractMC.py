def extractARMSMC(location):
    # file open
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
                if data_list.index('Use') == 2:
                    ARMS_robot.append(data_list[4])
                    i=i+1
        except ValueError:
            pass

    # close the file
    f.close()

    return ARMS_robot

MC = extractARMSMC('/workspace/test/AR_machine.const.txt')
print(MC)
