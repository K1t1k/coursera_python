def d_to_s(d):
	dic = {0: 'null', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
		5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
	return dic[d]

print(list(map(d_to_s, [1,2,3])))