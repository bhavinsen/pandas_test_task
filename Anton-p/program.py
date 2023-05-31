import pandas as pd
# filename = input("filename: ")
# if filename == 'nw_data.txt':
#     f = open(filename, "r")
#     print(f.read())
# else:
#     print("Enter valid filename")
    
flag=True
while flag:
    filename = input("Enter a filename for network data: ")

    if filename == 'nw_data.txt':
        display_social_network = input("Display the social network (y/n): ")
        if display_social_network == 'y':
            f = pd.read_csv(filename,  sep=" ")
            print(f)
            df = pd.DataFrame(f)
            index_list = []
            data = f
            flag1= True
            while flag1:
                member_id = input(" 1 Enter a Member id from 0 to 6: ")
                for i, idx in zip(df['friend_id'], df.index):
                    index_list.append(idx)
                print(type(member_id),'============ index_list =============',index_list)
                if int(member_id) in index_list:
                    data_members =  data.iloc[int(member_id)]['friend_id'].split(",")
                    if data_members == ['None']:
                        print(f"{member_id} has no friends")
                        continue
                        
                    output = []
                    for i in data_members:
                        for d in data.iloc[int(i)]['friend_id'].split(","):
                            output.append(d)
                    output1= list(set(output))
                    output2= output1.remove(member_id)
                    re_data = output1.copy()
                    for t in re_data:
                        if t in data_members:
                            output1.remove(t)
                    if output1 == []:
                        output1 = "none"
                        print(f"The recommended friend for {member_id} is {output1}")   
                    else:    
                        print(f"The recommended freind for {member_id} is {output1}")
                    # else:
                    #     print(f"{member_id} has no friends")
                else:
                    print('Member ID does not exist')
                    break
                    
                another_member = input("Do you want to recommend friends to another member (y/n) ")
                if another_member == 'y':
                    continue
                else:
                    break
                
            flag2 =True    
            while flag2:    
                display_friends = input("Display how many freinds member has (y/n) ")
                
                if display_friends == 'y':
                    member_id = input(" 2 Enter a Member id from 0 to 6: ")
                    friends =  data.iloc[int(member_id)]['friend_id'].split(",")
                    freinds_count = len(friends)
                    print(f"Member {member_id} has {freinds_count} friends")
                else:
                    break
            
            display_least_friends = input("Display the members with the least number of or have 0 friends (y/n) ")
            if display_least_friends == 'y':
                friends = []
                least_friends = []
                zero_friends_list = []
                df = pd.DataFrame(data)
                # print("----------df-------------",df)
                for i, idx in zip(df['friend_id'], df.index):
                    # print("-----------i---------------",i)
                    if i == "None":
                        # print("-----------None-222--------------",idx)
                        zero_friends = 0
                        zero_friends_list.append(idx)
                    else:  
                        count_least_friend = len(i.split(","))
                        # print("----count_least_friend-------",count_least_friend)
                        friends.append(count_least_friend)
                print("----friends-------",friends)
                smallest = min(friends)
                for f, d in zip(friends,df.index):
                    # print("----f-------",f)
                    if smallest == f:
                        # print("------ddd-----",d)
                        least_friends.append(d)
                print(f"The member ID for the member with least friend is:{least_friends}")        
                print(f"The member ID for the member with {zero_friends} is:{zero_friends_list}")
                
            while flag2:
                friends_of_friends = input("Display the friends of the friends of a given member (y/n) ") 
                
                if friends_of_friends == 'y':
                    member_id = input(" 3 Enter a Member id from 0 to 6: ")
                    # friends =  data.iloc[int(member_id)]['friend_id'].split(",")
                    df = pd.DataFrame(data)
                    # print("---------df--------------",df)
                    friends_of_friends_list = []
                    for i, idx in zip(df['friend_id'], df.index):
                        # print("-------------i-----------------",idx, i)
                        if int(member_id) == idx:
                            # print("------------member_id-------------", member_id, i)
                            # split_data = i.split(",")
                            friends_of_friends_list.append(i.split(","))
                            
                            
                    # print("-------------friends_of_friends_list---------",friends_of_friends_list)
                    for f in friends_of_friends_list:
                        # print("----fff------",f)
                        # d = f.split(",")
                        # for t in d:
                        #     print("----ttt-------",t)
                        for t in f:
                            member_data_list = []
                            member_id_list = []
                            new_member_list = []
                            # print("---------t-----------",t, i)
                            for j, idxx in zip(df['friend_id'], df.index):
                                # print("---------j-----------",idxx, j)
                                if int(t) == idxx:
                                    # print("------------t---------------",t)
                                    # print("------------j---------------",j)
                                    # print("------------member---------------",member_id)
                                    member_data_list.append(j.split(","))
                                    member_id_list.append(member_id)
                            # print("-------member_data_list------",member_data_list)
                            # print("---------member_id_list-----------",member_id_list)
                            for m in member_data_list:
                                # print("------m---------",m)
                                for q in m:
                                    # print("------q1---------",q)
                                    if q not in member_id_list:
                                        # print("-----if2--------",q)
                                        new_member_list.append(q)
                                if new_member_list:
                                    print(t,"->",new_member_list[0])
                                else:
                                    print(t,"-> none")
                            
                            # b = [elem for elem in member_data_list if elem not in member_id_list ]
                            # print("----------b--------------",b)

                break   

            flag=False
        else:
            break
    elif filename == 'nw_data2.txt':
        f = pd.read_csv(filename,  sep=" ")
        friends = []
        least_friends = []
        zero_friends_list = []
        df = pd.DataFrame(f)
        for i, idx in zip(df['friend_id'], df.index):
            if "," in i:
                count_least_friend = i.split(",")
                for j in count_least_friend:
                    friends.append((str(idx),j))
            else:
                friends.append((str(idx),i))
        res = [(sub[1], sub[0]) for sub in friends]
        for value in friends:
            if value not in res:
                print("The network is inconsitent, try another file")
        display_social_network = input("Display the social network (y/n): ")
        if display_social_network == 'y':
            f = pd.read_csv(filename,  sep=" ")
            print(f)
        break
    else:
        another_social_network = input(" dsfgdasgfdsagdasg (y/n): ")
        print("Enter valid filename")
        continue