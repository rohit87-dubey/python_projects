# we have to find out the cost of grass from land 
# where we have to deduct the area of home and area of garden from it
# cost of grass is Rs 10 per sqare feet

from loguru import logger

length_of_land = 100
breadth_of_land = 100

length_of_garden = 100
breadth_of_garden = 20

length_of_home = 80
breadth_of_home = 60

def calcuate_area(length, breadth):
    if length <= 0 or breadth <= 0:
        logger.error("Length and breadth should be greater than zero")
        return 0
    return length * breadth

area_of_land = calcuate_area(length_of_land, breadth_of_land)
area_of_garden = calcuate_area(length_of_garden, breadth_of_garden)
area_of_home = calcuate_area(length_of_home, breadth_of_home)

area_for_grass = area_of_land - (area_of_garden + area_of_home)
cost_of_grass = area_for_grass * 10

logger.info(f"Area for grass: {area_for_grass} sq feet")
logger.info(f"Cost of grass Rs: {cost_of_grass}")