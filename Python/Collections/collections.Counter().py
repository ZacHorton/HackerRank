from collections import Counter

if __name__ == "__main__":
    x = int(input())
    shoe_sizes_input = input()
    shoe_sizes = shoe_sizes_input.split(" ")
    inventory = Counter(shoe_sizes)
    n = int(input())
    counter, money_earned = 0, 0
    while counter < n:
        customer = input()
        request = customer.split(" ")
        for key, value in inventory.items():
            if key == request[0]:
                if value > 0:
                    money_earned += int(request[1])
                    inventory[key] -= 1
        counter += 1
    print(money_earned)
