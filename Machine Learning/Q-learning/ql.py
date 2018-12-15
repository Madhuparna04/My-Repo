'''		(0,0)(0,1)(0,2)
		 ___________
		|   |   |   |
   (0,0)|_S_|___|___|
		|   |   |XXX|
   (1,0)|___|___|XXX|
		|   |   |   |
   (2,0)|___|___|_G_| 

   Actions - 1:UP
   			 2:DOWN
   			 3:RIGHT
   			 4:LEFT

'''
import random
def game(state,action):
	'''
	Reward of -1 for all actions in states [0,0] , [0,1] ,[1,0] and [2,0]
	Reward of -10 for going into blocked state [1,2] (Represented by XXX)
	Reward of +10 for reaching the Goal
	'''

	#End of episode
	if state[0]==2 and state[1]==1 and action==3:
			return [10,[2,2]]

	elif state[0]==1 and state[1]==1 and action==3:
			return [-10,[1,1]]
	elif state[0]==0 and state[1]==2 and action==2:
			return [-10,[0,2]]
	
	else:
		if action==1:
			x=state[0]-1
			y=state[1]
			if x<0:
				x=0
			return [-1,[x,y]]
		elif action == 2:
			x=state[0]+1
			y=state[1]
			if x>2:
				x=2
			return [-1,[x,y]]
		elif action ==3:
			x=state[0]
			y=state[1]+1
			if y>2:
				y=2
			return [-1,[x,y]]
		else:
			x=state[0]
			y=state[1]-1
			if y<0:
				y=0
			return [-1,[x,y]]

def main():
	alpha=0.2
	epsilon=0.2
	discount=0.9
	Qvalue=[[[] for x in range(3)] for y in range(3)] 
	print("Qvalues initially :")
	print("	    	Actions")
	print("		UP DOWN RIGHT LEFT")
	for i in range(3):
		for j in range(3):
			if i==2 and j==2:
				Qvalue[i][j][:]= [0,0,0,0]
			else:
				Qvalue[i][j][:]= random.sample(range(5), 4)
			print("State (",i,",",j,") :",end="")
			for k in range(4):
				print(round(Qvalue[i][j][k],2),end=" ")
			print(" ")

	numgames=10000
	#Playing 100 games
	for i in range(numgames):
		#Starting with state (0,0)
		state=[0,0]
		rew=0
		#Loop untill terminal state
		while state!=[2,2]:
			randomnum= random.uniform(0,1)
			action=0
			if randomnum>=epsilon:
				lst=Qvalue[state[0]][state[1]]
				action=lst.index(max(lst))+1
			else:
				action=random.randint(1,4)
			
			#Play the game
			reward,nextstate = game(state,action)
			rew=rew+reward
			nxtlist=Qvalue[nextstate[0]][nextstate[1]]
			currval=Qvalue[state[0]][state[1]][action-1]
			Qvalue[state[0]][state[1]][action-1]= currval +  alpha * ( reward + discount*(max(nxtlist)) - currval)
			state=nextstate


	print("Qvalues after playing ",numgames," games :")
	print("	    	Actions")
	print("		UP DOWN RIGHT LEFT")
	for i in range(3):
		for j in range(3):
			print("State (",i,",",j,") :",end="")
			for k in range(4):
				print(round(float(Qvalue[i][j][k]),1),end="   ")
			print(" ")
	print()
	#Playing the game by choosing action with max Qvalue from each state encountered
	print("Playing Game :")
	state=[0,0]
	totalreward=0
	print("State[0,0] --->",end=" ")
	while state!=[2,2]:
		lst=Qvalue[state[0]][state[1]]
		action=lst.index(max(lst))+1
		print(action)
		reward,nxtstate=game(state,action)
		totalreward=totalreward+reward
		state=nxtstate
		print("State[",state[0],",",state[1],"] --->",end=" ")
		
	print("Total reward = ",totalreward)



if __name__=='__main__':
	main()



