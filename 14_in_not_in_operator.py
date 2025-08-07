numbers = [10,20,30,40,50]

num = int(input("Enter number")) //1

result = num in numbers
print(result)
asian_countries = [
    "Afghanistan",
    "Armenia",
    "Azerbaijan",
    "Bahrain",
    "Bangladesh",
    "Bhutan",
    "Brunei",
    "Cambodia",
    "China",
    "Cyprus",
    "Georgia",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Israel",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Lebanon",
    "Malaysia",
    "Maldives",
    "Mongolia",
    "Myanmar",
    "Nepal",
    "North Korea",
    "Oman",
    "Pakistan",
    "Palestine",
    "Philippines",
    "Qatar",
    "Saudi Arabia",
    "Singapore",
    "South Korea",
    "Sri Lanka",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Thailand",
    "Timor-Leste",
    "Turkey",
    "Turkmenistan",
    "United Arab Emirates",
    "Uzbekistan",
    "Vietnam",
    "Yemen"
]

country = input("Enter country")
result = country in asian_countries
print(result)

asian_countries_string = "Afghanistan Armenia Azerbaijan Bahrain Bangladesh Bhutan Brunei Cambodia China Cyprus Georgia India Indonesia Iran Iraq Israel Japan Jordan Kazakhstan Kuwait Kyrgyzstan Laos Lebanon Malaysia Maldives Mongolia Myanmar Nepal North Korea Oman Pakistan Palestine Philippines Qatar Saudi Arabia Singapore South Korea Sri Lanka Syria Taiwan Tajikistan Thailand Timor-Leste Turkey Turkmenistan United Arab Emirates Uzbekistan Vietnam Yemen"

result = country in asian_countries_string
print(result)

result = country not in asian_countries
print(result)

result = country not in asian_countries_string
print(result)
