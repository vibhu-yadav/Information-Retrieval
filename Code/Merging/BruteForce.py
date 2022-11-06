import sys

def preprocess():
    d = dict()
    n = len(sys.argv)
    for key, value in zip(sys.argv[1:n:2],sys.argv[2:n:2]):
        # d[key] = value
        indices = list(map(int, value.split(',')))
        d[key.lower()] = indices

    return d

def AND(key1,key2):

    print("AND")

    i = j = 0
    ans = []

    while (i < len(key1)) and (j < len(key2)):
        if key1[i] == key2[j]:
            ans.append(key1[i])
            i += 1
            j += 1
        elif key1[i] < key2[j]:
            i += 1
        else:
            j += 1

    return ans

def OR(key1,key2):


    print("OR")

    i = j = 0
    ans = []

    while (i < len(key1)) and (j < len(key2)):
        if key1[i] == key2[j]:
            ans.append(key1[i])
            i += 1
            j += 1
        elif key1[i] < key2[j]:
            ans.append(key1[i])
            i += 1
        else:
            ans.append(key2[j])
            j += 1

    while i < len(key1):
        ans.append(key1[i])
        i += 1

    while j < len(key2):
        ans.append(key2[j])
        j += 1

    return ans

def NOT(key1,key2):

    print("NOT")

    i = j = 0
    ans = []

    while (i < len(key1)) and (j < len(key2)):
        if key1[i] == key2[j]:
            i += 1
            j += 1
        elif key1[i] < key2[j]:
            ans.append(key1[i])
            i += 1
        else:
            j += 1

    while i < len(key1):
        ans.append(key1[i])
        i += 1

    return ans


def process(query,d):
    
    print("Processing Query: ",query)

    query = query.lower()

    queries = query.split(' ')

    if queries[1] == 'and':
        return AND(d[queries[0]],d[queries[2]])

    elif queries[1] == 'or':
        return OR(d[queries[0]],d[queries[2]])

    elif queries[1] == 'not':
        return NOT(d[queries[0]],d[queries[2]])


if __name__ == "__main__":


    d = preprocess()

    # for key,value in d.items():
    #     print(key,value)


    while True:

        print("To enter a query, press Y. To exit, press N.")       
    
        response = input()

        if response == 'N' or response == 'n':
            break

        elif response == 'Y' or response == 'y':
            print("Enter the query: ")
            query = input()

            print(process(query,d))