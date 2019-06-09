import os
import sys
import platform

#clear function
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    if platform.system() == 'Linux':
        os.system('clear')

#file saving
if platform.system() == 'Windows':
    osV = 0
if platform.system() == 'Linux':
    osV = 1

if osV == 0:
    os.chdir('C:/Program Files')
    try:
        os.mkdir('DFW-Profiles')
        os.chdir('DFW-Profiles')
        os.mkdir('Company Reports')
        os.mkdir('Person Reports')
    except FileExistsError:
        os.chdir('DFW-Profiles')

if osV == 1:
    os.chdir('/home')
    try:
        os.mkdir('DFW-Profiles')
        os.chdir('DFW-Profiles')
        os.mkdir('Company Reports')
        os.mkdir('Persons Reports')
    except FileExistsError:
        os.chdir('DFW-Profiles')





def print_menu():
    print(30 * "-" , "Doxing-Menu" , 30 * "-")
    print("[1]. Create a Profile about a Person")
    print("[2]. Create a Profile for a Company")
    print("[3]. Exit Doxing-Framework")
    print(67 * "-")

loop = True

while loop:
    print_menu()
    choice = input("Select From One of the Fallowing [1-3]: ")

    if choice == '1':
        clear()
        print("""\n\t'BASIC-INFO'
        	    \n
        	    \nEnter 'N/A' If It Doesn't Apply
        	    """)
        ssn = input("\nEnter the Target's 'SSN-#', like this 999-99-999: \n\n>")
        phonenumber = input("\nEnter the Target's 'Phone-Number', like this (999)999-9999: \n\n>")
        firstname = input("\nEnter the Target's 'FIRST NAME': \n\n>")
        middlename = input("\nEnter the Target's 'MIDDLE NAME': \n\n>")
        lastname = input("\nEnter the Target's 'LAST NAME': \n\n>")
        ethnicity = input("\nEnter the Target's 'Ethnicity': \n\n>")
        religion = input("\nEnter the Target's 'RELIGION': \n\n>")
        age = input("\nEnter the Target's 'AGE': \n\n>")
        dobm = input("\nEnter the Target's 'MONTH-OF-BIRTH': \n\n>")
        dobd = input("\nEnter the Target's 'DAY-OF-BIRTH': \n\n>")
        doby = input("\nEnter the Target's 'YEAR-OF-BIRTH': \n\n>")
        highschool = input("\nEnter the Name of the 'SCHOOL' where the Target Went to: \n\n>")
        highschooladdr = input("\nEnter the Target's 'SCHOOL-STREET-ADDRESS': \n\n>")
        highschooltown = input("\nEnter the 'Town' Where the School is: ")
        highschoolstate = input("\nEnter the 'State' Where the School is: \n\n>")
        highschoolzip = input("\nEnter the Target's 'SCHOOL-AREA-CODE': \n\n>")
        highschoolnumber = input("\nEnter the Target's 'SCHOOL-PHONE-NUMBER': \n\n>")
        highschoolemail = input("\nEnter the Target's 'SCHOOL-EMAIL-ADDRESS': \n\n>")
        highschoolgrad = input("\nEnter the Target's 'Graduation YEAR': \n\n>")
        jobplace = input("\nWhere Does the Target 'WORK'? \n\n>")
        jobposition = input("\nEnter the Target's job 'POSITION': \n\n>")
        workaddr = input("\nEnter the Target's WORK-STREET-ADDRESS': \n\n>")
        worktown = input("\nEnter The 'Town' Where the Target Worked: \n\n>")
        workstate = input("\nEnter the 'State' Where the Target Worked In: \n\n")
        workzip = input("\nEnter the Target's 'WORK-AREA-CODE': \n\n>")
        workphone = input("\nEnter the Target's 'WORK-PHONE-NUMBER': \n\n>")
        workemail = input("\nEnter the 'EMAIL' Where the Target Works: \n\n>")

        clear()

        #
        # Locations
        #
        print("""\n\t'LOCATIONS'
        	    \n
        	    \nEnter 'N/A' If It Doesn't Apply
        	    """)
        currentcountry = input("\nEnter the Target's Current 'COUNTRY': \n\n>")
        currentstate = input("\nEnter the Target's Current 'STATE/TERRITORY/PROVINCE': \n\n>")
        currenttown = input("\nEnter the Target's Current 'TOWN/CITY': \n\n>")
        currentzip = input("\nEnter the Target's Current 'ZIP-CODE': \n\n>")
        currentstreetaddr = input("\nEnter the Target's Current 'STREET-ADDRESS': \n\n>")
        pastcountry = input("\nEnter the Target's Past 'COUNTRY': \n\n>")
        paststate = input("\nEnter the Target's Past 'STATE/TERRITORY/PROVINCE': \n\n>")
        pasttown = input("\nEnter the Target's Past 'TOWN/CITY': \n\n>")
        pastzip = input("\nEnter the Target's Past 'ZIP-CODE': \n\n>")
        paststreetaddr = input("\nEnter the Target's Past 'STREET-ADDRESS': \n\n>")

        clear()

        #
        # Relationships
        #
        print("\n\t'RELATIONSHIPS'")
        print("\nEnter N/A if it Doesn't Apply")

        girlfriend = input("\nEnter the Target's 'GIRL-FRIEND/FIANCE/WIFE' Name: \n\n>")
        mother = input("\nEnter the Target's 'MOTHER'S' NAME': \n\n>")
        father = input("\nEnter the Target's 'FATHER'S' Name: \n\n>")

        clear()

        #
        # Accounts
        #
        print("""\n\t'ACCOUNTS'
        	    \nEnter 'N/A' If It Doesn't Apply
        	    \nIf Credential's Do Apply Enter It In Like the Following:
        	    \nUser-Name:[testing@yahoo.com]-Password:[test1234]""")

        aol = input("\nEnter the Target's 'AOL' Credentals: \n\n>")
        outlook = input("\nEnter the Target's 'OUTLOOK' Credentials: \n\n>")
        gmail = input("\nEnter the Target's 'GMAIL' Credentials: \n\n>")
        yahoo = input("\nEnter the Target's 'YAHOO' Credentials: \n\n>")
        facebooklink = input("\nEnter the Target's 'FACEBOOK-PROFILE-URL': \n\n>")
        facebook = input("\nEnter the Target's 'FACEBOOK' Credentials: \n\n>")
        twitterlink = input("\nEnter the Target's 'TWITTER-PROFILE-URL': \n\n>")
        twitter = input("\nEnter the Target's 'TWITTER' Crendtials: \n\n>")
        linkedinurl = input("\nEnter the Target's LINKEDIN-PROFILE-URL': \n\n>")
        linkedin = input("\nEnter the Target's 'LINKEDIN' Credentials: \n\n>")

        clear()

        #
        # Sources
        #
        print("""\n\t'SOURCES'
        	    \nEnter 'N/A' If It Doesn't Apply
        	    """)
        sources = input("\nEnter Any Sources about The Target\nif Any at the Prompt \n\nSources:\n\n ")

        clear()

        #
        # Summary/Notes
        #
        print("""\n\t'SUMMARY/NOTES'
        	    \nEnter 'N/A' If It Doesn't Apply
        	    """)
        notes = input("\nEnter Any Additional Info About the Target if Any at the Prompt \n\nNotes:\n\n ")

        clear()

        #
        # Useful Websites
        #
        print("""\n\t'Useful Websites'
        	    \nEnter 'N/A' If It Doesn't Apply
        	    """)
        usefulsites = input("\nEnter Any Useful Websites: \n\n ")

        clear()

        #
        # This Code Writes the Users
        # Input to a Text File
        #
        # import time
        ## dd/mm/yyyy format

        print("")


        doxprofile = input(
            "\nGive the Dox File a Name, \nPreferably with Target's First and Last Name-Dox-Profile.txt\n\n>")
        os.chdir('Person Reports')
        doxfile = open(doxprofile + '.txt', 'w')

        doxfile.write("[+] Basic Info")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t-> Social Security Number:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + ssn)
        doxfile.write("\n\n")
        doxfile.write("\t-> Phone-Number:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + phonenumber)
        doxfile.write("\n\n")
        doxfile.write("\t-> First Name:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + firstname)
        doxfile.write("\n\n")
        doxfile.write("\t-> Middle Name:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + middlename)
        doxfile.write("\n\n")
        doxfile.write("\t-> Last Name:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + lastname)
        doxfile.write("\n\n")
        doxfile.write("\t-> Ethnicity:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + ethnicity)
        doxfile.write("\n\n")
        doxfile.write("\t-> Religion:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + religion)
        doxfile.write("\n\n")
        doxfile.write("\t-> Age:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + age)
        doxfile.write("\n\n")
        doxfile.write("\t-> Date Of Birth")
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Month:" + dobm)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Day:" + dobd)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Year:" + doby)
        doxfile.write("\n\n")
        doxfile.write("\t-> High School:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + highschool)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Street Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + highschooladdr)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Town/City:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + highschooltown)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> State:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + highschoolstate)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Zip Code:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + highschoolzip)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Phone-Number:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + highschoolnumber)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Email-Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + highschoolemail)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Graduation Year:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + highschoolgrad)
        doxfile.write("\n\n")
        doxfile.write("\t-> Work:")
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Company:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + jobplace)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Positiion:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + jobposition)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Street Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + workaddr)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Town/City:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + worktown)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> State:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + workstate)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Zip Code:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + workzip)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Phone-Number:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + workphone)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Email-Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + workemail)
        doxfile.write("\n\n")
        doxfile.write("[+] Locations")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t-> Current")
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Country:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + currentcountry)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> State:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + currentstate)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Town/City:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + currenttown)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Zip Code:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + currentzip)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Street Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + currentstreetaddr)
        doxfile.write("\n\n")
        doxfile.write("\t-> Past")
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Country:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + pastcountry)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> State:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + paststate)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Town/City:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + pasttown)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Zip Code:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + pastzip)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Street Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + paststreetaddr)
        doxfile.write("\n\n")
        doxfile.write("[+] Relationships")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t-> Girlfriend/Wirfe/Fiance:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + girlfriend)
        doxfile.write("\n\n")
        doxfile.write("\t-> Mother:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + mother)
        doxfile.write("\n\n")
        doxfile.write("\t-> Father:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + father)
        doxfile.write("\n\n")
        doxfile.write("[+] Accounts")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t\t-> AOL:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + aol)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> OutLook:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + outlook)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Gmail:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + gmail)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Yahoo:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + yahoo)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Facebook:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t-> Facebook Profile URL" + facebooklink)
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + facebook)
        doxfile.write("\n\n")
        doxfile.write("\t\t->Twitter:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t-> Twitter Profile URL" + twitterlink)
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + twitter)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Linked:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t-> Linkedin Profile URL" + linkedinurl)
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + linkedin)
        doxfile.write("\n\n")
        doxfile.write("[+] Sources")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t\t->" + sources)
        doxfile.write("\n\n")
        doxfile.write("[+] Summary")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t\t->" + notes)
        doxfile.write("\n\n")
        doxfile.close()

        print("\n[+]...Dox-Profile Complete")

        cont = input("\n[!]...Press 'Return' to Continue")
        clear()



    if choice == '2':

        clear()
        print("""\n\t'COMPANY-INFO'
	    \n
	    \nEnter 'N/A' If It Doesn't Apply
	    """)
        compname = input("\nEnter the Company's 'NAME': \n\n>")
        compphone = input("\nEnter the Company's 'Phone-Number', like this (999)999-9999: \n\n>")
        compemail = input("\nEnter the Company's 'EMAIL' \n\n>")
        compcountry = input("\nEnter the 'COUNTRY' the Company Is In: \n\n>")
        compaddr = input("\nEnter the Company's 'STREET-ADDRESS': \n\n>")
        comptown = input("\nEnter The 'TOWN' Where the Company Is In: \n\n>")
        compstate = input("\nEnter the 'STATE' Where the Company Is Located: \n\n")
        compzip = input("\nEnter the Company's 'AREA-CODE': \n\n>")

        clear()

        #
        # Internet
        #
        print("""\n\t'INTERNET'
	    \nEnter 'N/A' If It Doesn't Apply
	    """)
        compsite = input("\nEnter the Company's Website: \n\n>")
        hoststate = input("\nEnter the Host's Online State [up/down]: \n\n>")
        openports = input("\nEnter any Open Ports On the Host System: \n\n>")
        filteredports = input("\nEnter and Filtered Ports On the Host System: \n\n>")
        closedports = input("\nEnter any Closed Ports On the Host System: \n\n>")
        portsscan = input("\nEnter and Ports You've Scanned: \n\n>")
        hostuptime = input("\nEnter the Host's Up Time: \n\n>")
        lastboot = input("\nEnter the Host's Last Known Boot: \n\n>")
        ipv4 = input("\nEnter the Host's IPV4 Address: \n\n>")
        ipv6 = input("\nEnter the Host's IPV6 Address: \n\n>")
        mac = input("\nEnter the Host's Mac Address: \n\n")
        os = input("\nEnter the Host's Operating System: \n\n>")
        acc = input("\nEnter Host's Operating System Guess Accurcy: \n\n>")
        portinfo = input("""\nEnter any Running Ports, Port-State and Protocol on the Host System,
	    \nLike this:
	    \n\n21-[openssh-server-vs.2.91]-[Open] \n\n>
	    """)
        compsmtp = input("\nEnter the Company's 'SMTP' Server-Address: \n\n>")
        compsmtpport = input("\nEnter the Company's 'SMTP-PORT': \n\n>")
        osclass = input("\nEnter the Host's Operating System Class: \n\n>")
        osvender = input("\nEnter the Host's Operating System Vender [Ubuntu,Microsoft,Mac, etc.]: \n\n>")
        osfamily = input("\nEnter the Host's Operating System Family: \n\n>")
        osgeneration = input("\nEnter the Host's Operating System Generation: \n\n>")
        osgenacc = input("\nEnter Host's Operating System Generation Guess Accurcy: \n\n>")

        clear()

        #
        # Sources
        #
        print("""\n\t'SOURCES'
	    \nEnter 'N/A' If It Doesn't Apply
	    """)
        sources = input("\nEnter Any Sources about the Company at the Prompt \n\nSources:\n\n ")

        clear()

        #
        # Summary/Notes
        #
        print("""\n\t'SUMMARY/NOTES'
	    \nEnter 'N/A' If It Doesn't Apply
	    """)
        notes = input("\nEnter Any Additional Info About the Company if Any at the Prompt \n\nNotes:\n\n ")

        clear()

        #
        # Useful Websites
        #
        print("""\n\t'Useful Websites'
	    \nEnter 'N/A' If It Doesn't Apply
	    """)
        usefulsites = input("\nEnter Any Useful Websites: \n\n ")

        clear()

        #
        # This Code Writes the Users
        # Input to a Text File
        #
        # import time
        ## dd/mm/yyyy format

        doxprofile = input("\nGive the Dox File a Name, \nPreferably with with Company's Name-Dox-Profile.txt\n\n>")
        os.chdir('Company Reports')
        doxfile = open(doxprofile + '.txt', 'w')

        doxfile.write("[+] Company Info")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t-> Company Name:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + compname)
        doxfile.write("\n\n")
        doxfile.write("\t-> Phone-Number:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + compphone)
        doxfile.write("\n\n")
        doxfile.write("\t-> Email-Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + compemail)
        doxfile.write("\n\n")
        doxfile.write("[+] Location")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t\t-> Country:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + compcountry)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> State:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + compstate)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Town/City:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + comptown)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Zip Code:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + compzip)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Street Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + compaddr)
        doxfile.write("\n\n")
        doxfile.write("[+] Internet")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t-> Company Site:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + compsite)
        doxfile.write("\n\n")
        doxfile.write("\t-> Host State:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + hoststate)
        doxfile.write("\n\n")
        doxfile.write("\t-> Open Ports:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + openports)
        doxfile.write("\n\n")
        doxfile.write("\t-> Filtered Ports:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + filteredports)
        doxfile.write("\n\n")
        doxfile.write("\t-> Closed Ports:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + closedports)
        doxfile.write("\n\n")
        doxfile.write("\t-> Ports Scanned:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + portsscan)
        doxfile.write("\n\n")
        doxfile.write("\t-> Uptime:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + hostuptime)
        doxfile.write("\n\n")
        doxfile.write("\t-> Last Boot:")
        doxfile.write("\n\n")
        doxfile.write("\t\t->" + lastboot)
        doxfile.write("\n\n")
        doxfile.write("\t-> Addresses:")
        doxfile.write("\n\n")
        doxfile.write("\t\t-> SMTP:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + compsmtp)
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + compsmtpport)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> IPV-4:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + ipv4)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> IPV-6:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + ipv6)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> MAC-Address:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + mac)
        doxfile.write("\n\n")
        doxfile.write("\t-> Operating System:")
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Operating System Name:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + os)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Accuracy")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + acc)
        doxfile.write("\n\n")
        doxfile.write("\t-> Ports Used:")
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Port:Version:State")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + portinfo)
        doxfile.write("\n\n")
        doxfile.write("\t-> Operating System Class:")
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Class:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + osclass)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> OS Vender:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + osvender)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> OS Family:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + osfamily)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> OS Generation:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + osgeneration)
        doxfile.write("\n\n")
        doxfile.write("\t\t-> Accuracy:")
        doxfile.write("\n\n")
        doxfile.write("\t\t\t->" + osgenacc)
        doxfile.write("\n\n")
        doxfile.write("[+] Sources")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t\t->" + sources)
        doxfile.write("\n\n")
        doxfile.write("[+] Summary")
        doxfile.write("\n")
        doxfile.write("-" * 80)
        doxfile.write("\n")
        doxfile.write("\n")
        doxfile.write("\t\t->" + notes)
        doxfile.write("\n\n")
        doxfile.close()

        print("\n[+]...Dox-Profile Complete")

        cont = input("\n[!]...Press 'Return' to Continue")



    if choice == '3':
        print("\nThanks for Using Doxing-FrameWork")
        loop = False