def create():
    print("Hello, I am Kirtan !!!!")
create()


def name(n):
    print(f"Hey,{n}")

name("Kirtan")
#_____________________________________________


# Program : Portfolio

# Dictionary storing personal and professional details using key-value pairs
Info = {
    "Name": "Kirtan Parmar",                  # String value
    "Age": 18,                                # Integer value
    "Address": "Anand, Gujarat, India",       # String value
    "Qualification": "Diploma : Computer Engineering",  # String value
    "Skills": {                               # Nested dictionary
        "Languages": ["Python", "Dart", "C++"],  # List of strings
        "Frameworks": ["Flutter"],             # List of strings
        "Database": ["MySQL", "SQLite"]        # List of strings
    },
    "College": "B & B Institute Of Technology, VVN"  # String value
}

# Define a function named portfolio
def portfolio():
    print("----- My Portfolio -----\n")        # Print a header
    
    # Loop through each key-value pair in the Info dictionary
    for key, value in Info.items():            # .items() returns key and value
    
        # Check if the value is a dictionary (nested dictionary)
        if type(value) == dict:
            print(f"{key}:")                    # Print the key
            
            # Loop through each key-value in the nested dictionary
            for sub_key, sub_value in value.items():
                # Join the list items into a comma-separated string and print
                print(f"  {sub_key}: {', '.join(sub_value)}")
        else:
            # If value is not a dictionary, print key and value normally
            print(f"{key}: {value}")

# Call the function to run the portfolio display
portfolio()
