if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        # Read the command and split it into parts
        # e.g., "insert 0 5" becomes ["insert", "0", "5"]
        command_parts = input().split()
        cmd = command_parts[0]
        
        if cmd == "insert":
            my_list.insert(int(command_parts[1]), int(command_parts[2]))
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            my_list.remove(int(command_parts[1]))
        elif cmd == "append":
            my_list.append(int(command_parts[1]))
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()
            
            
            