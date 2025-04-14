import math
def painting_wall(height , width , cover):
    area = height * width
    total_con = math.ceil(area / cover)
    print(f"you'll need {total_con} of piant ")
    
    
    
h = int(input("Enter the hight"))
w = int(input("Enter the width"))
coverage = 5
painting_wall(height = h , width = w , cover = coverage)


