def main():
    ## Display colleges from requested state.
    colleges = getOrderedListOfColleges()
    displayListOfColleges(colleges)
    
def getOrderedListOfColleges():
    infile = open("Colleges.txt", 'r')
    colleges = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(colleges)):
        colleges[i] = colleges[i].split(",")
        colleges[i][2] = int(colleges[i][2])
    
    colleges.sort(key=lambda college: college[2])
   
    return colleges

def displayListOfColleges(colleges):
    found = False
    abbrev = input("Enter a state abbreviation: ")
    for college in colleges:
        #college = college.split(",")
        if college[1].lower() == abbrev.lower():
            print(college[0], college[2])
            found = True
    if not found:
        print("There are no early colleges from", abbrev + '.')
    
main()
