# Calculate the perimeter and the area of the garden
# pay the fair price for that.

# The prices for the fences and lawns.
fencePrice =  3 # per meter.
lawnPrice = 2 # per square meter.

# You need the foreman.
foreman = hero.findNearest(hero.findFriends())
corners = foreman.corners

# Get the information about the garden.
bottomLeft = corners.bottomLeft
topRight = corners.topRight

# Calculate the size of the garden.
width = topRight.x - bottomLeft.X
height = topRight.y - bottomLeft.y

# Find the perimeter of the garden (meters).
perimeter = 2*width + 2*height

# Use fencePrice and calculate the fence cost:
fenceCost = fencePrice*perimeter

# Find the area of the garden (square meters).
area = width * height

# Use lawnPrice to calculate the lawn cost.
lawnCost = area * lawnPrice

# The total cost is the sum of the fence and the lawn costs.
totalCost = fenceCost + lawnCost

hero.say("The total price is " + totalCost)
foreman.bill(totalCost)