import turtle
import pandas

screen = turtle.Screen()
screen.title("African Countries Puzzle")
screen.bgpic("afro_img1.gif")

data = pandas.read_csv("countries.csv")
all_countries = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < 51:
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/51 countries", prompt="What's another country's name?").title()
    if answer_country == "Exit":
        missing_countries = []
        for country in all_countries:
            if country not in guessed_countries:
                missing_countries.append(country)
            new_data = pandas.DataFrame(missing_countries)
            new_data.to_csv("Countries to learn")
        break

    if answer_country in all_countries:
        guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(float(country_data.x), float(country_data.y))
        t.write(answer_country)
