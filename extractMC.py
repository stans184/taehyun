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
        
        # if data_list.index('Robot') == 0 and data_list.index('In') ==1
        # if 'Robot' and 'In' and 'Use' in data_list
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
