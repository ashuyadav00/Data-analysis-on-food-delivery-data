import os
import sys

def function():
	file = open(os.path.join(sys.path[0], "text_file.txt"), "r")

	list1 = []
	for i in file:
		a1 = i.split(',')
		list1.append(a1)	

	total_amount_of_order = 0
	for i in list1:
		j = 1
		total_amount_of_order +=  int(list1[j][3])
		j += 1


	unique = {}	
	table = {}
	for i in list1[1:]:
		if (i[1], i[2]) in table:
			table[i[1], i[2]] += 1

		elif (i[1], i[2]) != " ":
			table[i[1], i[2]] = 1	

		else:
			table[i[1]] = 0

			
			
	order_1, order_2, order_3, order_4, order_5, name_of_one_order, name_of_two_order, name_of_three_order, name_of_four_order, name_of_five_order = 0,0,0,0,0,[],[],[],[],[]



	for keys, values in table.items():
		if values == 1:
			order_1 += 1
			name_of_one_order.append(keys[1])
		elif values == 2:
			order_2 += 1
			name_of_two_order.append(keys[1])	
		elif values == 3:
			order_3 += 1
			name_of_three_order.append(keys[1])
		elif values == 4:
			order_4 += 1
			name_of_four_order.append(keys[1])
		else: 
			order_5 += 1
			name_of_five_order.append(keys[1])

	x = ['order_1','order_2','order_3','order_4','order_5']
	order_number_list = [order_1, order_2, order_3, order_4, order_5]

	Total_number_of_order = len(list1)-1
	return (Total_number_of_order, total_amount_of_order, order_number_list, name_of_one_order, name_of_two_order, name_of_three_order, name_of_four_order, name_of_five_order)


