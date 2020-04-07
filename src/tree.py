class Tree:

  def __init__(self, address, species, diam, condition, exposure, near_building, building_year, distance_to_building, direction_to_building):
    self.address = address
    self.species = species
    self.diam = diam
    self.condition = condition
    self.exposure = exposure
    self.near_building = near_building
    if near_building:
      self.building_year = building_year
      self.distance_to_building = distance_to_building
      self.direction_to_building = direction_to_building
