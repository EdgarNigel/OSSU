import math

def polysum(n, s):
    
    area = (0.25*n*s*s) / math.tan(math.pi/n)
    perimeter = n * s
    
    polysum = area + perimeter**2
    
    return float("{0:.4f}".format(polysum))
	
	

