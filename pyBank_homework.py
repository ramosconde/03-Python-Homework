# import dependencies
import csv

# define the path to the file
file_path = "PyBank_Resources_budget_data.csv"
saveFile = open("PyBank_output.txt", "a")
#saveFile.write(text)
#saveFileaveFile.close()

# initialize variables to hold our values
count = 0							#Row counter
revenue = 0							#Profit/Loss sum 
revenue_change_list = []			#Keeps the amount of revenue change from previous year to the next
month_list = []						# first_row, name of the months and year

# open file and load data with new name  'revenue_data'

with open(file_path) as revenue_data:
	# use the Reader function from the CSV data
	# constructs a list of the csv file containing all info
	reader = csv.reader(revenue_data)

	# skip the header row
	first_row = next(reader)

	# loop through each row
	for row in reader:
		# count number of months
		count += 1

		# sum of revenue
		revenue += int(row[1])

		if count == 1:
			# previous revenue is assigned as the first row revenue value
			previous_revenue = int(row[1])

		else:
			# calculate the change in revenue
			revenue_change = int(row[1]) - previous_revenue

			# assign the current row to be used in next iteration
			previous_revenue = int(row[1])

			# save the calculation to the revenue change list column. append will add the calculation to the bottom of the list
			revenue_change_list.append(revenue_change)

			# save the month name of the current row to a list. The append will ADD the name to the bottom of the list
			month_list.append(row[0])

# calculate the average revenue change
average_revenue_change = sum(revenue_change_list)/len(revenue_change_list)


print("\n\n\nFinancial Analysis  ")
print("_______________________________________________________")
print("\nTotal Months: \t\t\t" + str(count))
print("Total: \t\t\t\t$", (revenue))
print("Average revenue change is: \t$", round(average_revenue_change, 2))

increase = max(revenue_change_list) # gives the greatest revenue increase
incr_index = revenue_change_list.index(increase) # give the index in which the max value occurred

print("Greatest Increase in Profits: \t"+ month_list[incr_index]  +"   ("+ str(increase),")")

decrease = min(revenue_change_list) # gives the greatest revenue decrease
decr_index = revenue_change_list.index(decrease) # give the index in which the max value occurred

print("Greatest Decrease in Profits: \t"+  month_list[decr_index] + "   (" + str(decrease),")")
print("\n\n\n")

#----------------------------------------------------------------------------------------------------
text =("\n\n\n\t\t\tFinancial Analysis  \n")
saveFile.write(text)
text1 =("_______________________________________________________\n")
saveFile.write(text1)
text2 =("Total Months: \t\t\t" + str(count))
saveFile.write(text2)
text3=("\nTotal: \t\t\t\t$"+ str(revenue))
saveFile.write(text3)
text4=("\nAverage revenue change is: \t$"+ str(round(average_revenue_change, 2))+"\n")
saveFile.write(text4)
text5=("Greatest Increase in Profits: \t"+ month_list[incr_index]  +"   ("+ str(increase)+")")
saveFile.write(text5)
text6=("\nGreatest Decrease in Profits: \t"+  month_list[decr_index] + "   (" + str(decrease)+")")
saveFile.write(text6)
text7=("\n\n\n")
saveFile.write(text7)

saveFile.close()



