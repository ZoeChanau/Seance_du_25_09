import numpy as np
import matplotlib.pyplot as plt

x = 10*np.random.random(50)
y = linear(x, (1,3))

def linear(x, params=(0,1)):
    a, b = params[1], params[0]
    return b+a*x+5*np.random.normal(size=len(x))

def linear_hypothesis(x, params=(0,1)):
    a, b = params[1], params[0]
    return b+a*x

def gradient_descent(x, y, params, alpha=0.001, iterations=1000):
	"Fonction qui "
	for i in range(iterations) :
		params[0] = params[0] - (alpha/N)*sum(linear_hypothesis(x, params) -y)
		"alpha = le pas. Plus le pas est petit plus la fonction sera precise et plus elle mettra de temps a converger / Plus le pas est grand et plus vite elle convergera au detriment de la precision."
		params[1] = params[1] + (alpha/N)*(linear_hypothesis(x, params) -y).dot(x)
		"Le produit scalaire peut remplacer la somme pour le params[1]"
	return params

plt.scatter(x,y)
plt.plot(x,p[0]+p[1]*x)
plt.figure()
#plt.ylim(ymax=50)
plt.plot(np.arange(len(error_history)), error_history[:,0])
plt.title("Erreur")
plt.figure()
plt.plot(error_history[:,1], error_history[:,2])
plt.title("Parametres")
plt.xlabel("b")
plt.ylabel("a")
plt.show()
