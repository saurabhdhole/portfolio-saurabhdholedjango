from django.db import models

# Create your models here.

class Project:
  def __init__(self,id, name, role, technology, description):
    self.id = id
    self.name = name
    self.role = role
    self.technology = technology
    self.description = description
