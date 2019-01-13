# import dependencies
import csv
import os
#import print_function

# define the path to the file
file_path = os.path.join("PyPoll_Resources_election_data.csv")
saveFile = open("PyPoll_output.txt", "a")


vote_total = 0							#Row/total vote counter
canidate_name = []
counter={}			

with open(file_path) as vote_data:
	# constructs a list of the csv file containing all info
	csvreader = csv.reader(vote_data)
	
	# skip the header row
	first_row = next(csvreader)
					
	for row in csvreader:
		vote_total+=1
		if row[2] in counter:
			counter[row[2]]+=1
		else:
			counter[row[2]]=1


w = 0
print("""\n\n\n\n\t\tElection Results 
_____________________________________________________""")
print ("\n\t\tTotal Votes:   ", "\t", vote_total )
print("_____________________________________________________\n")
#*********THIS PARAGRAPH ACTUALY WORKS ************
for i in sorted(counter.values()):
	c=(list(counter.keys())[::-1][list(counter.values()).index(i)])
	p=("{00:.3f}%".format(list(counter.values())[::-1][list(counter.values()).index(i)]/vote_total*100))
	t=(list(counter.values())[::-1][list(counter.values()).index(i)])
	if t > w:
		w = t
	if len(c) >= 6:
		print(c, ":\t", p, "\t\t(", t, ")")
	else:
		print(c, ":\t\t", p, "\t\t(", t, ")")
print("_____________________________________________________\n")

inverse_name = [(value, key) for key, value in counter.items()]
winning_candidate = max(inverse_name)[1]

print("Winner:****", winning_candidate, "**** Total Votes Reveived: ", w)									

print("\n_____________________________________________________")
print("\n\n\n\n")


text=("\n\n\n\n\t\tElection Results ")
saveFile.write(text)
text1=("\n_____________________________________________________")
saveFile.write(text1)
text2=("\n\t\tTotal Votes:   "+ "\t"+ str(vote_total) )
saveFile.write(text2)
text3=("\n_____________________________________________________")
saveFile.write(text3)
for i in sorted(counter.values()):
	c=(list(counter.keys())[::-1][list(counter.values()).index(i)])
	p=("{00:.3f}%".format(list(counter.values())[::-1][list(counter.values()).index(i)]/vote_total*100))
	t=(list(counter.values())[::-1][list(counter.values()).index(i)])
	if t > w:
		w = t
	if len(c) >= 6:
		#print(c, ":\t", p, "\t\t(", t, ")")
		text3a="\n" +(str(c) + ": \t"+ str(p)+ "\t\t("+ str(t) + ")")
		saveFile.write(text3a)
	else:
		#print(c, ":\t\t", p, "\t\t(", t, ")")
		text3b="\n" +(str(c) + ": \t\t"+ str(p) + "\t\t("+ str(t) + ")")
		saveFile.write(text3b)
		
text4=("\n_____________________________________________________")
saveFile.write(text4)
text5=("\nWinner:****"+ str(winning_candidate) + "**** Total Votes Received: "+ str(w))									
saveFile.write(text5)
text6=("\n_____________________________________________________")
saveFile.write(text6)
text7=("\n\n\n\n")
saveFile.write(text7)

saveFile.write(text7)

saveFile.close()


# increase = max(revenue_change_list)							# gives the greatest revenue increase
# incr_index = revenue_change_list.index(increase) 			# give the index in which the max value occurred









