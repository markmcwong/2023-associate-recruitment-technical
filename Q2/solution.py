# Read data from input file
# allValid = true
# errorCodes = []
# for each record in input file:
#     allValid = record.isValid
#     if record.isValid is not true:
#         errorCodes append error message

# if allValid is true:
#     print "Yes"
# else:
#     print "No"
#     print errorCodes sepearated by space character


class Record():
    def __init__(self, isValid, error = None):
        self.isValid = isValid
        self.error = error


def main():
    num_of_recs = int(input())
    errorCodes = []
    allValid = True

    for i in range(num_of_recs):
        args = input().split()
        # records.append(Record(*args[1:]))
        allValid = allValid and (args[1] == 'true')
        if args[1] == 'false':
            errorCodes.append(args[2])
    
    if(allValid):
        print("YES")
    else:
        print('No')
        print(' '.join(errorCodes))
    return

if __name__ == "__main__":
    main()
