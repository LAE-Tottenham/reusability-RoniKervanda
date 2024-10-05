# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
import math 
def get_triangle_sides(triangle_number):
    "get the opposite and adjacent sides of a triangle from users input"
    opp = float(input("Enter your triangle's opposite side length: "))
    adj = float(input("Enter your triangles's adjacent side length: "))
    return opp, adj 

def calculate_hypotenuse(opp, adj):
    "calculate the hypotenuse given the adjacent and opposite sides"
    return math.sqrt(opp**2 + adj**2)

def weird_calculation():
    "perform the weird calculation"
    "get the sides from the first and second triangles"
    opp1, adj1 = get_triangle_sides(1)
    opp2, adj2 = get_triangle_sides(2)
    
    "calculate the hypotenuse for both triangles"
    hyp1 = calculate_hypotenuse(opp1, adj1)
    hyp2 = calculate_hypotenuse(opp2, adj2)
    
    "create a third triangle using the hypotenuses of the triangles"
    hyp3 = calculate_hypotenuse(hyp1, hyp2)

    return hyp3 
    
    
            
    
# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################

def weird_calculation():
    # get the length and width of the first triangle from the user
    opp1 = float(input("Enter your first triangle's opposite side length: "))
    adj1 = float(input("Enter your first triangle's adjacent side length: "))

    # work out the hyp
    import math
    hyp1 = math.sqrt(opp1**2 + adj1**2)

    # get the length and width of the second triangle from the user
    opp2 = float(input("Enter your second triangle's opposite side length: "))
    adj2 = float(input("Enter your second triangle's adjacent side length: "))

    # work out the hyp
    import math
    hyp2 = math.sqrt(opp2**2 + adj2**2)

    # create a third triangle with the hyp1 as the opp and hyp2 as the adj
    opp3 = hyp1
    adj3 = hyp2
    
    import math
    hyp3 = math.sqrt(opp3**2 + adj3**2)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
valid user input, if  a non-numeric value is entered the float() would be an error
lengths must be positive 
correct use of math.sqrt(), it cannot be negative 

# 2. Validate the user's input based on your preconditions.
import math 
def get_triangle_sides(triangle_number):
    "get the opposite and adjacent sides of a triangle from users input"
    opp = float(input("Enter your triangle's opposite side length: "))
    adj = float(input("Enter your triangles's adjacent side length: "))
    if opp > 0 and adj > 0:
        print("Sides are valid")
        return opp, adj 
    else:
        print("Sides are invalid")
        exit()

def calculate_hypotenuse(opp, adj):
    "calculate the hypotenuse given the adjacent and opposite sides"
    return math.sqrt(opp**2 + adj**2)

def weird_calculation():
    "perform the weird calculation"
    "get the sides from the first and second triangles"
    opp1, adj1 = get_triangle_sides(1)
    opp2, adj2 = get_triangle_sides(2)
    
    "calculate the hypotenuse for both triangles"
    hyp1 = calculate_hypotenuse(opp1, adj1)
    hyp2 = calculate_hypotenuse(opp2, adj2)
    
    "create a third triangle using the hypotenuses of the triangles"
    hyp3 = calculate_hypotenuse(hyp1, hyp2)

    return hyp3 
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise. 
it is useful because we only have one input function which prveents duplication, which makes the code easier to maintain, for example if 
the formula to find out hypotenuse changes, all releveant calculations reflect the change
resuable components like get_triangle_sides, calculate_hypotenuse, weird_calculation makes it easier to understand and read, allowing the
user to not get confused and when resitting the code as the names clearly indicate what each function is for ‹

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
