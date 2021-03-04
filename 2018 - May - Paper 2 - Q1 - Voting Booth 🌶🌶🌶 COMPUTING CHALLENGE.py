# variables
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#vote counts for the candidates
CandA = 0 #candidate A
CandB = 0 #candidate B
CandC = 0 #candidate C

#candidate names
#CandA_name = input("candidate a") #candidate A
#CandB_name = input("candidate b") #candidate B
#CandC_name = input("candidate c") #candidate C

#hard coded candidate names
CandA_name = "candidate a" #candidate A
CandB_name = "candidate b" #candidate B
CandC_name = "candidate c" #candidate C

#votecounts
CANDIDATES = [CandA, CandB, CandC]
totalVotes = CandA + CandB + CandC

#voter variables
name = "" # current voter
names = [] #names of all the people who've voted

#quick write strings
currentVotes = str(CANDIDATES[0]) +"--> "+ CandA_name +" "+ str(CANDIDATES[1]) +"--> "+ CandB_name +" "+ str(CANDIDATES[2]) +"--> "+ CandC_name
#--------------------------------------------------------------------------------------------------------------------------------------------------


#functions
def br(): # new line
    print("\n")


#main loop
while name != "END":
    
	#name entry
    print("what is your name")
    name = input()
    
	#checking for SYSTEM COMMAND: LOGOUT
	if name == "END":
        break
    br()
    
	#voting choice
    print("who are you voting for " + CandA_name +" or "+ CandB_name +" or "+ CandC_name)
    vote = input()
    
	#candidate a
    if vote == "candidate a":
        CandA = CandA + 1
        CANDIDATES = [CandA, CandB, CandC]
        currentVotes = str(CANDIDATES[0]) +"--> "+ CandA_name +" "+ str(CANDIDATES[1]) +"--> "+ CandB_name +" "+ str(CANDIDATES[2]) +"--> "+ CandC_name
        print(currentVotes)
    
	#candidate b
    elif vote == "candidate b":
        CandB = CandB + 1
        CANDIDATES = [CandA, CandB, CandC]
        currentVotes = str(CANDIDATES[0]) +"--> "+ CandA_name +" "+ str(CANDIDATES[1]) +"--> "+ CandB_name +" "+ str(CANDIDATES[2]) +"--> "+ CandC_name
        print(currentVotes)
    
	#candidate c
    elif vote == "candidate c":
        CandC = CandC + 1
        CANDIDATES = [CandA, CandB, CandC]
        currentVotes = str(CANDIDATES[0]) +"--> "+ CandA_name +" "+ str(CANDIDATES[1]) +"--> "+ CandB_name +" "+ str(CANDIDATES[2]) +"--> "+ CandC_name
        print(currentVotes)
    
	else: #incorrect data voiding
        print("VOID")
		
    #once the voter has voted it calls the next voter
    print("NEXT VOTER")
    br()


# updating the log variables 
CANDIDATES = [CandA, CandB, CandC]
currentVotes = str(CANDIDATES[0]) +"--> "+ CandA_name +" "+ str(CANDIDATES[1]) +"--> "+ CandB_name +" "+ str(CANDIDATES[2]) +"--> "+ CandC_name
totalVotes = CandA + CandB + CandC

#dumping most recent data
print("total votes", totalVotes)
print(currentVotes)
