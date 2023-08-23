#Import os module

import os



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

        

first_name=os.environ.get('First_Name')

last_name=os.environ.get('Last_Name')

if first_name is None or last_name is None:

    print("Error: first name or last name is not set")

    exit(-1)

if not first_name.isalpha() or not last_name.isalpha():

    print("Error: first name and last name must be alphabatical")

    exit(1)

#first creating tmp2 directory for the second part

create_dir("tmp2")

os.chdir("tmp2")

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

    f1.close()

    f2.close()

    

    

    

