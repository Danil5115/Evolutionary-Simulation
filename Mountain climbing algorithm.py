import random

M = 30 # backpack capacity
    #kg, cost
a = [(3, 150), (4, 250), (2, 100), (6, 300), (1, 50), (5, 200), (3, 150), (4, 250), (2, 100), (6, 300), (1, 50), (5, 200), (3, 150), (4, 250), (2, 100), (6, 300), (1, 50), (5, 200), (3, 150), (4, 250), (2, 100), (6, 300), (1, 50), (5, 200), (3, 150), (4, 250), (2, 100), (6, 300), (1, 50), (5, 200)]

#We calculate the cost of the backpack and its weight Bereme v úvahu náklady na batoh a jeho váhu
def backpack_value(alpha, a, M):
    cost, weight = 0, 0
    for i, (w, c) in enumerate(a):
        if alpha[i] == "1":
            if weight + w <= M:
                weight += w
                cost += c
            else:
                cost -= c
                weight += w
    return cost

#Randomly compose a binary list of items in the backpack Náhodně sestavte binární seznam položek v batohu
def random_alpha(size):
    return "".join([str(random.randint(0, 1)) for i in range(size)])

#Mutate members from this backpack Zmutujte členy z daného batohu
def mutation(alfa, pmut):
    return "".join(str(1 + int(alfa[i]) * -1) if random.random() < pmut else alfa[i] for i in range(len(alfa)))

def hill_climb(f, tmax, k, c0, pmut):
    f_max = 0
    alpha_max = None
    alpha = random_alpha(k)
    for attempt in range(tmax):
        U = [mutation(alpha, pmut) for i in range(c0)]  #Creates a list of 10 mutation options
        alpha = max(U, key=lambda alpha: f(alpha)) 
        f_x = f(alpha)
        if f_x > f_max:
            f_max =  f_x
            alpha_max = alpha
        print(f"Attempt: {attempt}, alpha: {alpha}, f: {f_x}, best: {f_max}")
    return (alpha_max, f_max)

print(hill_climb(lambda alpha: backpack_value(alpha, a, M), tmax=100, k=len(a), c0=10, pmut=0.25))
