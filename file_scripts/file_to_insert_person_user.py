import re


GIRL_NAMES = 'Lisa Dianne Mazie Joni Susan Barbara Elizabeth Debbie Amy Claire Deb Jeanne Kelly Kirsten Heidi Patty Maria Shelley Moore Tammy'


# Will return a unique username by appending an index in case a user name alread exist.
def get_username(username_list, first, last):
    username = first[0].lower() + last.lower()
    count = 0
    while (username in username_list):
        count += 1
        username += count
    return username


def insert_person(last_name, first_name, gender, dob):
    insert_person = """INSERT INTO person (person_id, last_name, first_name, gender, dob)
    VALUES (person_seq.NEXTVAL, '{}', '{}', '{}', DATE '{}');\n""".format(last_name, first_name, gender, dob)
    print(insert_person)

def insert_user(username_list, first_name, last_name):
    username = get_username(username_list, first_name, last_name)
    insert_user = """INSERT INTO app_user(user_id, username, person_id) 
    VALUES (app_user_seq.NEXTVAL, '{}', person_seq.CURRVAL);\n""".format(username)
    print(insert_user)

def insert_senator(cls):
    insert_senator = """INSERT INTO senator(senator_id, person_id, class_id) 
    VALUES (senator_seq.NEXTVAL, person_seq.CURRVAL, {});\n\n""".format(cls)

    print(insert_senator)


filename = '/Users/royce/github/learn-sql/oracle/setup/us_senators_AUG2016.txt' 
with open(filename, 'r') as f:
    count = 0
    username_list = []

    for line in f:
        # print(line,end='')
        count += 1
        # print(count)
        
        state, name, dob, cls = line.strip().split(', ')
        first_name, last_name = re.findall(r'((?:\w+ )*)(\w+)$', name)[0]
        gender = 'F' if first_name in GIRL_NAMES else 'M'
        first_name = first_name.strip()

        insert_person(last_name, first_name, gender, dob)
        insert_user(username_list, first_name, last_name)
        insert_senator(cls)

print("Total: {}".format(count))

