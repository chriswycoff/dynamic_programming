# implementation of milepost problem ###

# Writen by Christopher Wycoff ###

# USAGE: python3 milepost.py

import math

#mile_posts = [0,50,200,210,300,430,500,530,600,720,800]
	
#mile_posts = [0,100,200,300,400,500,605]

mile_posts = [0,105,125,225,250,350,450,550]

#mile_posts = [0,100,175,200,275,375,475,575,675]

def main(mile_posts):

	num_mile_post = len(mile_posts)

	optimal = [0]* (num_mile_post)

	posts_to_use = []

	for i in range(1, num_mile_post):
		new_min = math.inf
		for j in range(0,i):
			number_to_consider = optimal[j] + (100 - (mile_posts[i] - mile_posts[j]))**2
			if number_to_consider < new_min:
				new_post = j
				optimal[i] = number_to_consider
				new_min = number_to_consider

		posts_to_use.append(new_post)


	print(optimal)

	the_next = posts_to_use[-1]
	
	final_posts_to_use = []
	final_posts_to_use.insert(0,the_next)

	while True:
		the_next = posts_to_use[the_next-1] 

		if the_next == 0:
			break

		final_posts_to_use.insert(0,the_next)

	final_posts_to_use.insert(0,0)

	print(posts_to_use)

	print(final_posts_to_use)








if __name__ == "__main__":
	main(mile_posts)
