graph = {}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


graph[input('Enter root role name : ')] = []
flag = True

while flag:

    print('Operation :\n\t1. Add Sub Role\n\t2. Display Roles\n\t3. Delete Role\n\t4. Add User\n\t5. Display Users ')
    choice = int(input('Operation to be performed : '))
    if choice == 1:
        subrole = input('Enter sub role name : ')
        reportrole = input('Enter reporting to role name : ')
        print("Enter the role to be deleted : ")
        username = input("Add User : ")
        role = input("Enter role : ")

        if reportrole not in graph.keys():
            graph[reportrole] = []
        else:
            val = graph[reportrole]
            val.append(subrole)
            graph[reportrole] = val
            if subrole not in graph.keys():
                graph[subrole] = []

            if username not in graph[reportrole] or graph[subrole] and role in graph[reportrole] or graph[role]: #Add user
                val = graph[role]
                val.append(username)
                graph[reportrole] = val


    elif choice == 3:
        if subrole in graph.keys():
            val = graph[subrole]
            val.pop(subrole)
        graph[subrole] = val






else:
    bfs(visited, graph, 'CEO')
    flag = False
