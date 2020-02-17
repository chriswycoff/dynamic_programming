# rod_problem

# Christopher Wycoff


rod_len = 10

rod_price_for_len = [(1,1),(2,5),(3,8),(4,9),(5,10),
				(6,17),(7,17),(8,20),(9,24),(10,30),]


def rod_optimizer(rod_len, rod_price_for_len):

	opt_price_list = [0] * (rod_len + 1)

	for i in range(1,rod_len + 1):
		for j in range(i):
			opt_price_list[i] = max(opt_price_list[i], rod_price_for_len[j][1]\
				+ opt_price_list[i-j-1])

	return opt_price_list


def main():
	r = rod_optimizer(rod_len,rod_price_for_len)

	print(r)

	

if __name__ == "__main__":
	main()




