import queue

class Shirt():
    def __init__(self, size):
        self.size = size

    def fulfill_order(self, required_size):
        if (required_size == self.size):
            return True
        elif ('L' in required_size and 'M' in self.size):
            return False
        elif('S' in self.size and ('L' in required_size or 'M' in required_size)):
            return False
        elif self.size.count('X') > required_size.count('X') and 'L' in self.size and 'L' in required_size:
            return True
        elif self.size.count('X') < required_size.count('X') and 'S' in self.size and 'S' in required_size:
            return True
        else:
            return False

    def __eq__(self, other):
        if(other.size == self.size):
            return True
        else:
            return False

    def __lt__(self, other):
        if(self.size == 'M' and other.size == 'L'):
            return True
        elif('S' in self.size and ('L' in other.size or 'M' in other.size)):
            return True
        elif self.size.count('X') < other.size.count('X') and 'L' in self.size and 'L' in other.size:
            return True
        elif self.size.count('X') > other.size.count('X') and 'S' in self.size and 'S' in other.size:
            return True
        else:
            return False

def main():
    number_of_t_shirts = input()
    t_shirt_sizes = input()
    number_of_requests = input()
    request_sizes = input()

    t_shirt_sizes = t_shirt_sizes.split()
    request_sizes = request_sizes.split()

    shirts = list(map(lambda x: Shirt(x), t_shirt_sizes))
    shirts.sort()

    if(number_of_requests > number_of_t_shirts):
        print("NO")
        return

    for i in request_sizes:
        fulfill = False
        for j in shirts:
            if(j.fulfill_order(i)):
                shirts.remove(j)
                fulfill = True
                break
        if(not fulfill):
            print("NO")
            return
    
    print("YES")
    return

if __name__ == "__main__":
    main()
