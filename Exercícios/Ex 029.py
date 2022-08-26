v = float(input('Speed (in km/h): '))
if v > 80:
    print("Speedy, ain'tcha? You owe the state {:.2f} dollars, pal.".format(7*(v - 80)))
else:
    print("Howdy, partner. Move along.")
