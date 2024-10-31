# We want to estimate the size of a Burleous Majoris
# Find the average size of this burl population to use as a baseline

# This function returns the average size of all the burls in an array.
def averageSize(burl):
    sum = sumSize(burls)

    # Average = Sum / Amount
    return sum / burls.length

# This function returns the sum of all the burls sizes
def sumSize(burls):
    # Implement the sum function using the burls 'size':
    totalsize = 0

    for burl in burls:
        totalSize += burl.size
    return totalSize

# The main function
def main():
    while True:
        burls = hero.findByType("burl")
        averageSizeValue = averageSize(burls)

        hero.say(averageSizeValue)
        