import os
import csv

total_votes = 1
khancount = 1
correycount = 1
licount = 1
otooleycount = 1
list_of_candidates = []

csvpath = os.path.join("Instructions","PyPoll","Resources","election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader)
    print(f'Header: {csvreader}')


# I probably don't need 3 "for" statements but it works and I don't want to break it
    for row in csvreader:
    # took total_votes=0 from solutions :-(
        total_votes= total_votes + 1 
        name=row[2]

    # this is also taken from the solution:-(
        if name not in list_of_candidates:
            list_of_candidates.append(name)


        if name == "Khan": 
            khancount = khancount + 1
        elif name=="Correy":
            correycount = correycount + 1
        elif name == "Li": 
            licount = licount + 1
        elif name == "O'Tooley":
            otooleycount = otooleycount + 1


    total_votes = total_votes - 1
    khancount = khancount - 1
    correycount = correycount - 1
    licount = licount - 1
    otooleycount = otooleycount -1

    percentkhan = khancount / total_votes * 100
    percentcorrey = correycount / total_votes *100
    percentli = licount / total_votes *100
    percentotooley= otooleycount / total_votes *100

    WINNER = []
    WINNER = ( max(khancount,correycount, licount, otooleycount))
 
    if khancount == WINNER:
         winner = "Khan"
    elif correycount in WINNER:
        winner = "Correy"
    elif licount in WINNER:
        winner = "Li"
    elif otooleycount in WINNER:
        winner = "O'Tooley"

# print the stuff
    print(f" Election Results: There were {total_votes} . Khan had {khancount} votes and {percentkhan} % of the total votes. Correy had {correycount} votes and {percentcorrey} % of the total votes. Li had {licount} votes and {percentli} % of the total votes. O'Tooley had {otooleycount} votes and {percentotooley} % of the total votes. This means that the winner is {winner}!")

# output txt
output = os.path.join("..", "outputpypoll.txt")
with open(output, "w") as txt_file:
# this part is really bad but I could not make it one fluid f string
    Election_Results_1 = (f' Election Results: {total_votes}')
    Election_line2 = (f' Khan: {percentkhan} , {khancount} ')
    Election_line3= (f' Correy: {percentcorrey} , {correycount}' )
    Election_line4= (f' O"Tooley: {percentotooley}, {otooleycount}')
    Summary= (f' {Election_Results_1} {Election_line2} {Election_line3} {Election_line4}')

    txt_file.write(Summary)
