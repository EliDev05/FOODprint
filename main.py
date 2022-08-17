from time import sleep

import openai

#insert your API key there
openai.api_key = ""

#AI personality
personality = ("I am a highly intelligent environmental question answering bot. "
               "If you ask me a question about the environment, I will give you the answer."
               " If you ask me a question that is nonsense, trickery, or has no clear answer,"
               " I will respond with \"Error\".\n\n")

#Examples for AI
qa_examples = ("Q: What's the CO2 emission of Olio Carli?\n"
               "A: 5.5 kg/Liter\n\n"

               "Q: What's the rating of Olio Carli based on his emission?\n"
               "A: 8/10\n\n"

               "Q: What's the description of Olio Carli based on his emission?\n"
               "A: Olio Carli is a brand of olive oil that is produced in Italy. "
               "The olives are grown in a region that has a lot of sunlight, "
               "which reduces the need for artificial lighting.\n\n"
                
               "Q: What's the description of Coca Cola based on his emission?\n"
               "A: Coca Cola is a brand of soda that is produced in the United States. "
               "The company uses a lot of water and energy to produce its drinks, which results in a large amount of carbon dioxide emissions.\n\n"
               
               "Q: How much CO2 I save by buying CocaCola?\n"
               "A: 40%\n\n"

               "Q: How many squigs are in a bonk?\n"
               "A: Error.\n\n"

               "Q: Is my playstation recyclable?\n"
               "A: Yes, Sony (playstation) has a recycling program.\n\n"

               "Q: What is the square root of banana?\n"
               "A: Error.\n\n"

               "What's the CO2 emission of Coca Cola?\n"
               "A: 2.5 kg/Liter\n\n"

               "Q: Give a rating of Coca Cola emissions\n"
               "A: 5/10\n\n"

               "Q: Give a rating of Nesquik emissions.\n"
               "A: 4/10\n\n"

               "Q: Give a rating of Beyond Meat emissions.\n"
               "A: 3/10\n\n"

               "Q: Give a rating of Green Toys emissions.\n"
               "A: 9/10\n\n"

               "Q: Give a rating of Wipro EcoEnergy emissions.\n"
               "A: 7/10\n\n"

               "Q: Give a rating of Olio Carli emissions.\n"
               "A: 8/10\n\n"

               "Q: What's the description of Beyond Meat based on his emission?\n"
               "A: Beyond Meat is a company that produces plant-based meat products. "
               "The company's products have a lower carbon footprint than traditional meat products because they require less water and land to produce.\n\n"

               "Q: What's the description of Wipro EcoEnergy based on his emission?\n"
               "A: Wipro EcoEnergy is a company that provides energy-efficient solutions. "
               "The company's products have a lower carbon footprint because they use less energy.\n\n"

               "Q: What's the CO2 emission of Beyond Meat?\n"
               "A: 1.5 kg/Burger\n\n"

               "Q: rate pepsi\n"
               "A: 3/10\n\n"

               "Q: rate olio carli\n"
               "A: 8/10\n\n"

               "Q: emission olio carli\n"
               "A: 5.5 kg/Liter\n\n"

               "Q: emission pepsi\n"
               "A: 2.5 kg/Liter\n\n"

               "Q: How much co2 i save by buying cocacola?\n"
               "A: 40%\n\n"

               "Q: How much co2 i save by buying pepsi?\n"
               "A: 30%\n\n"

               "Q: How much co2 i save by buying dr pepper?\n"
               "A: 20%\n\n")


def co2_emission(product):
    question = "Q: " + product + " co2 emission\n"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=qa_examples + question,
        temperature=0,
        max_tokens=120,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    co2_emission.emission = float(response["choices"][0]["text"][3:][0:3])

    print("Emissions: " + response["choices"][0]["text"][3:])


def co2_rating(product):
    question = "Q: " + product + " co2 rating\n"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=qa_examples + question,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print("Rating: " + response["choices"][0]["text"][3:])


def co2_description(product):
    question = "Q: " + product + " co2 description\n"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=qa_examples + question,
        temperature=0,
        max_tokens=120,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print("Brand description: " + response["choices"][0]["text"][3:])


def co2_saved(product):
    question = "Q: " + product + " co2 saved\n"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=qa_examples + question,
        temperature=0,
        max_tokens=120,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    percentage = float(response["choices"][0]["text"][3:][:-1])
    saved = round(float((percentage/100)*co2_emission.emission), 1)

    print("kg of co2 saved: " + str(saved) + "kg")


while 1:
    product = input("\nWrite the product or brand name to see its data: ")

    co2_emission(product)
    sleep(3)                        #This is for give some time to API and AI for send data
    co2_rating(product)
    sleep(3)
    co2_description(product)
    sleep(3)
    co2_saved(product)
    sleep(3)
