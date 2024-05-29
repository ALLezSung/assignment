import csv  
  
def write_teams_to_csv(teams, filename='output\Teams.csv'):  
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:  
        fieldnames = ['队伍名称', '队长姓名', '队长电话']  
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
  
        writer.writeheader()  
        for team in teams:  
            writer.writerow(team)  
  
def write_members_to_csv(members, filename='output\Members.csv'):  
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:  
        fieldnames = ['姓名', '身份', '电话', '学号']  
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
  
        writer.writeheader()  
        for member in members:  
            writer.writerow(member)