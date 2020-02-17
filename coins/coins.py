# coins


coins = [1,5,6,8]

amount = 11


def fewest_coins_to_make_change(amount, coins):

	best_list = [amount+1] * (amount+1)

	best_list[0] = 0 # base case

	for i in range(1, amount+1):
		for coin in coins:
			if coin <= i:
				best_list[i] = min(best_list[i], best_list[i-coin]+1)

	return best_list


def main():
	c = fewest_coins_to_make_change(amount,coins)

	print(c)

	

if __name__ == "__main__":
	main()





