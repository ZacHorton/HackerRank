import cmath

if __name__ == "__main__":
    polar_nums = str(cmath.polar(complex(input())))
    print(polar_nums[1:-1].replace(", ", "\n"))
