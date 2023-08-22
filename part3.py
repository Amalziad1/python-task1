import os

import argparse



def help():

    print("Help Message: ")

    print("  -f   First name ")

    print("  -l   Last name ")

    print("  [ -c  Capitalize the first letter of the first and last name ] ")

    print("  [ -H   Display this help message ]")

parser=argparse.ArgumentParser()

parser.add_argument('-f', '--first_name')

parser.add_argument('-l', '--last_name')

parser.add_argument('-c', '--capitalize', action='store_true')

parser.add_argument('-H', '--help_message', action='store_true')



try:

    args = parser.parse_args()

    if args.help_message:

        help()

        exit(0)

    if args.first_name is None or args.last_name is None:

        print("Error: missing first name or last name")

        help()

        exit(1)

    if not args.first_name.isalpha() or not args.last_name.isalpha():

        print("Error: names must only contain alphabetical characters")

        help()

        exit(1)

    first_name = args.first_name

    last_name = args.last_name

    if args.capitalize:

        first_name = first_name.capitalize()

        last_name = last_name.capitalize()

except argparse.ArgumentError as e:

    print("Error:", e)

    help()

#===================================

def create_dir(dirname):

    #Check the directory name exist or not

    if os.path.isdir(dirname) == False:

        #Create the directory

        os.mkdir(dirname)

        #Print success message

        print("The directory is created.")

    else:

        #Print the message if the directory exists

        print("The directory already exists.")

        



#first creating tmp2 directory for the second part

create_dir("tmp3")

os.chdir("tmp3")

#then creating 5 directories

for i in range(5):

    dirname="training_project_"+str(i+1)

    create_dir(dirname)

    os.chdir(dirname)

    #writing in text files

    filename1="module_"+str(i+1)+"_"+"a.txt"

    filename2="module_"+str(i+1)+"_"+"b.txt"

    f1=open(filename1,"w")

    f1.write("Hello "+first_name+" "+last_name+" welcome to file "+str(i+1)+".A\n")

    f2=open(filename2,"w")

    f2.write("Hello "+first_name+" "+last_name+" welcome to file "+str(i+1)+".B\n")

    #returning to tmp directory

    current_directory = os.getcwd()

    #get the parent directory by splitting the path and taking all but the last part

    parent_directory = os.path.dirname(current_directory)

    #change the current working directory to the parent directory

    os.chdir(parent_directory)

    

    

    

