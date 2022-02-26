import re
import json

regex = r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+"

#check email is Human or Non Human
def check_type(email):
        text = email.split("@")
        if "." in text[0] or len(text[0]) >= 8:
            return "Human"
        else:
            return "Non-Human"


#create output file in json format
def create_output(data,result_file):
    with open("result.json", "w") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
        print(f"Json file has been created. Check {result_file} file!")


#find email in the file
def email_finder(filename):
    result = {}

    with open(filename,'r', encoding="utf8") as f:  
        #check each line for email
        for line in f:
            items = re.findall(regex, line)

            for item in items:
                #if email already exist increase the occurance value
                if item in result.keys():
                    result[item]["Occurance"] += 1
                else:
                    result[item] = {
                        "Occurance" : 1,
                        "EmailType": check_type(item)
                    }

    return result

    
def main():
  emails = email_finder(filename = "websiteData.txt")
#   print(emails)
  create_output(data = emails, result_file = "result.json")


if __name__ == '__main__':
    main()


