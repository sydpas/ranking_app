def friends():
    name_list = []
    rank_list = []
    reason_list = []

    print("To quit, press space.")

    while True:
        name = input("Please enter a name: ")
        if name == " ":
            break

        rank = input("Please rank this individual from 1-100: ")
        if rank == " ":
            break

        reason = input("Why? ")
        if reason == " ":
            break

        name_list.append(name)
        rank_list.append(rank)
        reason_list.append(reason)

    return list(zip(name_list, rank_list, reason_list))  # pairs each name with its corresponding rank



