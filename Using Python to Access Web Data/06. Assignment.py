if __name__ == '__main__':
    N = int(input())
    output_list = []
    for _ in range(N):
        operation, *value = input().split()
        print(operation)
        print(value)
        if operation == 'insert':
            output_list.insert(int(value[0]), int(value[1]))
        if operation == 'print':
            print(output_list)
        if operation == 'remove':
            output_list.remove(int(value[0]))
        if operation == 'append':
            output_list.append(int(value[0]))
        if operation == 'sort':
            output_list.sort()
        if operation == 'pop':
            output_list.pop()
        if operation == 'reverse':
            output_list.reverse()