from bot.gmail_reg import GmailBot
import json
import random
import string

if __name__ == "__main__":
    #open json file to load driver and url
    with open('config.json') as file:
        config = json.load(file)

    driver = config['driver']
    url = config['url']
    number = config['number']

    #open file with list of first names
    #pick randomly one first name out of given json file
    with open('firstname.json') as file:
        config = json.load(file)

        def random_name(conf_file: list[str]):
            for _ in range(1):
                name = random.choice(conf_file)
            return name

    #open file with list of last names
    #pick randomly one last name out of given json file
    with open('lastname.json') as lfile:
        lconfig = json.load(lfile)

        def random_lname(conf_file: list[str]):
            for _ in range(1):
                lname = random.choice(conf_file)
            return lname

    firstName: str = random_name(config)
    lastName: str = random_lname(lconfig)


    # creates random name without domain affiliation
    def random_mail():
        rand_num = (random.randrange(100, 1000, 3))
        return f'{firstName}.{rand_num}.{lastName}'


    #10 symbols password generator
    def random_pass_gen():
        alphabet = list(string.ascii_letters)
        digits = list(string.digits)
        special_characters = list("!@#$%^&*()")
        alph = random.choices(alphabet, k=6)
        dgt = random.choices(digits, k=2)
        spchar = random.choices(special_characters, k=2)
        rand_list = alph + dgt + spchar
        random.shuffle(rand_list)
        return ''.join(rand_list)

    randPass = random_pass_gen()
    randMail = random_mail()

    #create structured json file for futur load of random user
    data= []
    data.append({
        'first name': firstName,
        'last name': lastName,
        'email': f'{randMail}@op.pl',
        'password': randPass})

    with open(f'{randMail}.json', 'w') as outfile:
        json.dump(data, outfile)

    GmailBot(driver,url,number,firstName,lastName,randMail,randPass)
