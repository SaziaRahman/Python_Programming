import os.path
import json


def file_inout():
    file_option = input("Options for file (Add/Search/Delete): ")
    if file_option == "Add":
        persons = {}
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender(Male/Female): ")
        persons[f"{name}"] = {"name": f"{name}", "age": f"{age}", "gender": f"{gender}"}
        print(persons)
        s = json.dumps(persons, indent=2)
        if os.path.exists("persons_accurate.txt"):
            st = ""
            with open("persons_accurate.txt", "r") as f:
                for line in f:
                    st = st + f"{line}"
            with open("persons_accurate.txt", "w+") as filein:
                if st == "":
                    filein.write(s)
                    print("----------------1st Entry----------------")
                else:
                    filein.write(st[:-1] + "," + s[1:])
                    print("----------------Added-----------------")
            with open("persons_accurate.txt", "r") as file:
                information = json.loads(file.read())
                for key in information:
                    print(f"The person's name is {information[key]['name']} who is "
                          f"{information[key]['age']} years old and gender is {information[key]['gender']}.")
        else:
            with open("persons_accurate.txt", "w") as file:
                file.write(s)
    elif file_option == "Search":
        Search = input("Enter your name to search: ")
        if os.path.exists("persons_accurate.txt"):
            st = ""
            with open("persons_accurate.txt", "r") as f:
                for line in f:
                    st = st + f"{line}"
            with open("persons_accurate.txt", "r") as file:
                if not Search in st:
                    print("The person's name is not found.")
                else:
                    information = json.loads(file.read())
                    print(f"The person's name is {information[Search]['name']} who is "
                          f"{information[Search]['age']} years old and gender is {information[Search]['gender']}.")
        else:
            print("The file is not found.")
    elif file_option == "Delete":
        Delete = input("Enter your name to delete: ")
        if os.path.exists("persons_accurate.txt"):
            st = ""
            with open("persons_accurate.txt", "r") as f:
                for line in f:
                    st = st + f"{line}"
            with open("persons_accurate.txt", "w+") as file:
                if st == "":
                    print("The person's name is not found.")
                else:
                    information = json.loads(st)
                    print(f"The person named {information[Delete]['name']} is is Deleted.")
                    del information[Delete]
                    new_file = json.dumps(information, indent=2)
                    file.write(new_file)
        else:
            print("The file is not found.")


if __name__ == "__main__":
    file_inout()