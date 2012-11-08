# -*- coding: utf-8 -*-
from pygame import Rect

"""
This world.py file is the internal representation of the world map for the SRES
simultor. The base idea is a grid, up to width x height. This information is
not exposed to the robots.

"""

class NullWorld(object):
  """NullWorld is just a world with no obstacles or tiles. Multiple robots can be
  found."""
  def __init__(self, length, width, robots):
    """Creates a new null world with a length, a width, and a list of robots

    Args:
      length: Length (will be converted to an int with floor)
      width: Width (will be converted to an int with floor)
    """
    self.length = int(length)
    self.width = int(width)
    self.robots = {r.id: r for r in robots}
    self.hitbox = Rect(0, 0, self.width, self.length)

  def teleport(self, robot_id, x, y):
    """Safely teleports a robot a certain location. I.E, if another robot is
    occupying that space, it will be checked.

    System is probably not perfect as we tend to use `pygame.Rect` to
    approximate our hitbox. As long as the collision detection methods of
    `pygame.Rect` is implemented, we should be okay.

    Args:
      robot_id: The id of the robot from robot.id
      x: the x coordinate of the center of the robot after teleport
      y: the y coordinate of the center of the robot after teleport

    Returns:
      True if teleport is successful, False if not.

    Raises:
      KeyError if robot_id is not found
    """
    if not self.hitbox.collidepoint(x, y):
      return False

    robot_to_be_moved = self.robots[robot_id]
    for robot in self.robots.values():
      if robot_id == robot.id:
        continue

      if robot.hitbox.colliderect(robot_to_be_moved.hitbox):
        return False

    robot.hitbox.centerx = x
    robot.hitbox.centery = y
    return True

