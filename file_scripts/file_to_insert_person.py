import re


GIRL_NAMES = 'Lisa Dianne Mazie Joni Susan Barbara Elizabeth Debbie Amy Claire Deb Jeanne Kelly Kirsten Heidi Patty Maria Shelley Moore Tammy'

filename = '/Users/royce/github/learn-sql/oracle/setup/us_senators_AUG2016.txt' 
with open(filename, 'r') as f:
    count = 0
    for line in f:
        print(line, end='')
        count += 1

        state, name, dob = line.strip().split(', ')[0:3]        
        first_name, last_name = re.findall(r'((?:\w+ )*)(\w+)$', name)[0]

        gender = 'F' if first_name in GIRL_NAMES else 'M'

        output = "INSERT INTO person (person_id, last_name, first_name, gender, dob)" \
                 "  VALUES (person_seq.NEXTVAL, '{}', '{}', '{}', DATE '{}');\n".format(last_name, first_name.strip(), gender, dob)
        
        print(output)

print("Total: {}".format(count))

