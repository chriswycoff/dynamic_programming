#knapshack

# Christopher Wycoff


W = 100

values_weight_pairs = [('a',10,5),('b',30,10),('c',20,15)]

def knapsack(W:int, values_weight_pairs:list):

	K = [0] * (W+1)

	n = len(values_weight_pairs)

	dict_of_values = {}

	for w in range(W+1):
		for i in range(n):
			w_i = values_weight_pairs[i][2]
			v_i = values_weight_pairs[i][1]
			if w_i <= w:
				K[w] = max(K[w], K[w-w_i]+ v_i)

				
	return K


def main():
	k = knapsack(W,values_weight_pairs)

	print(k, len(k))

	print(k[W])
	



if __name__ == "__main__":
	main()



