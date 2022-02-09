import os
import subprocess
import time
my_env = os.environ.copy()
climber_path = my_env["CLIMBERDIR"]

exp_id = 0
state = ""

while (exp_id < 10):

    #read state file
    try:
        file_state = open("state.txt", "r")
        state = file_state.readline().rstrip()
        file_state.close()
    except:
        print ("error reading state file")

    if (state == "grasshopper finished"):
        print ("docker starting")
        file = open("climber_inst.sh", "w")
        line1= "echo running climber\n"
        line2= "${CLIMBERDIR}/sh/rms.sh GlyP_G6P GlyP_AMP > morphx.al1\n"
        line3= "${CLIMBERDIR}/sh/morphx.sh GlyP_"+str(exp_id)+" GlyP_AMP 10"
        file.writelines([line1, line2, line3])
        file.close()
        state = "docker starting"

        subprocess.call(["bash", climber_path+'/examples/RUN101/climber_inst.sh'])
        exp_id +=1
        state = "docker finished"
        try:
            file_state = open("state.txt", "w")
            print (state)
            file_state.writelines([state])
            file_state.close()
        except:
            print ("error reading state file2")
    else:
        print (state)


    time.sleep(60)
    print ("waited a minute")



#subprocess.run(["bash", climber_path+'/examples/RUN101/climber_inst.sh', test])
#subprocess.run(["bash", climber_path+"/sh/rms.sh","GlyP_G6P","GlyP_AMP", ">","morphx.al1"])
#subprocess.run(["bash", climber_path+'/examples/RUN101/climber_inst.sh', test])





