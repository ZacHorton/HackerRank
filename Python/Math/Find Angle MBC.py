import math

if __name__ == '__main__':
  AB, BC = int(input()), int(input())

  MC = math.sqrt(AB**2 + BC**2) / 2
  # Hypotenuse divides right angled triangles into two isoceles triangle so AM=BM=CM
  BM = MC
  
  # Law of Sines (i.e. Side, Side, Angle)
  a = (math.sin(math.radians(45))/BM)*MC
  b = round(math.degrees(math.asin(a)))

  print(f"{b}{chr(176)}")
