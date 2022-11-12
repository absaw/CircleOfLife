######################################################
#       Main file of Project  -  Used to call all agents
######################################################


from AgentOneSimulator import *
from AgentTwoSimulator import *
from AgentThreeSimulator import *
from AgentFourSimulator import *
from AgentFiveSimulator import *
from AgentSixSimulator import *
from AgentSevenSimulator import *
from AgentEightSimulator import *

if __name__=="__main__":

    ch=-1
    while ch!=0:

        print("\n\nPress choice number for agent. 0 to exit")
        print(" 1 = Agent One")
        print(" 2 = Agent Two")
        print(" 3 = Agent Three")
        print(" 4 = Agent Four")
        print(" 5 = Agent Five")
        print(" 6 = Agent Six")
        print(" 7 = Agent Seven")
        print(" 8 = Agent Eight \n\n")
        ch=input("Enter choice->> ")
        print()
        if ch=="1":
            print("Started Agent One Simulator->\n")
            simulate_agent_one()
        elif ch=="2":
            print("Started Agent Two Simulator->\n")
            simulate_agent_two()
        elif ch=="3":
            print("Started Agent Three Simulator->\n")
            simulate_agent_three()
        elif ch=="4":
            print("Started Agent Four Simulator->\n")
            simulate_agent_four()
        elif ch=="5":
            print("Started Agent Five Simulator->\n")
            simulate_agent_five()
        elif ch=="6":
            print("Started Agent Six Simulator->\n")
            simulate_agent_six()
        elif ch=="7":
            print("Started Agent Seven Simulator->\n")
            simulate_agent_seven()
        elif ch=="8":
            print("Started Agent Eight Simulator->\n")
            simulate_agent_eight()
        elif ch=="7b":
            print("Started Agent Seven Defective Drone Simulator->\n")
            # simulate_agent_seven()
        elif ch=="8b":
            print("Started Agent Eigth Defective Drone Simulator->\n")
            # simulate_agent_()
        elif ch=="9":
            print("Started Agent Nine Simulator->\n")
            # simulate_agent_()
        elif ch=="0":
            print("Exiting. Thank you! ->\n")
            break
        else:
            print("Invalid Input")
    




