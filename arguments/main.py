# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

"_______________________________Part 1: Greet Template____________________________________"


def greet(name, greet = "Hello, <name>!"):
    output = greet.replace("<name>", name)
    return output

print(greet("Zelda"))
print(greet("Bob", "What's up, <name>!"))

"____________________________________Part 2: Force________________________________________"

def force(mass, body="earth"):
    celestial_body = {
        "sun" : 274,
        "jupiter" : 24.9,
        "neptune" : 11.2,
        "saturn" : 10.4,
        "earth" : 9.8,
        "uranus" : 8.9,
        "venus" : 8.9,
        "mars" : 3.7,
        "mercury" : 3.7,
        "moon" : 1.6,
        "pluto" : 0.6
    }
    return round(mass * celestial_body[body],1)

print(force(10, "mercury"))
print(force(20, "saturn")) 

"___________________________________Part 3: Gravity_______________________________________"

def pull(m1, m2, d):
    gravity = 6.674 * (10 ** -11)
    #print(gravity)
    gravitational_pull = (gravity * m1 * m2)/(d ** 2)
    return gravitational_pull

print("____________________example 2 cars_________________________")
print(pull(800, 1500, 3))
print("_________________example earth & apple_____________________")
print(pull(5972*10**24, 0.1, 6371*10**6))