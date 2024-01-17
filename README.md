# Szymon Mirczak
Projekt nr. 3 
do 21.01.2024 22:00

## Graph 1
```python3
K = 100000  # max quantity
r = .4      # growth factor

t0 = 75     # starting point
tf = 115    # limit point
interval = 1000 

timeline = np.linspace(t0, tf, interval) 
h = abs(timeline[1] - timeline[0]) # difference between two time points

# Gompertz equation
gompertz = np.zeros(interval)
gompertz[0] = 10

for i in range(1, interval):
    gompertz[i] = gompertz[i-1] + h * r * gompertz[i-1] * np.log(K/gompertz[i-1])

# Verhult equation
verhulst = np.zeros(interval)
verhulst[0] = 10

for i in range(1, interval):
    verhulst[i] = verhulst[i-1] + h * r * verhulst[i - 1] * (1 - verhulst[i-1]/K)    


# Visual graph
plt.plot(timeline, gompertz, label='Równanie Gompertza')
plt.plot(timeline, verhulst, label='Równanie Verhulsta')
plt.ylabel('Quantity of population')
plt.xlabel('Time')
plt.title('Comparison of Gompertz and Verhulst equations (1st graph)')
plt.legend()
plt.show()
```
porównując równania Gompertza oraz Verhulsta jesteśmy w stanie zauważyć różne podejście do wzrostu populacji. We wzorze Gompertza szybciej pojawia się wzrost oraz jest on szybszy niż we wzorze Verhulsta

## Graph 2
Korzystając z parametrów z podpunktu "a" zauważamy, że obie populacje obu gatunków rosną względem stanu początkowego oraz docierają do pewnego stanu równowagi gdzie oba gatunki przeżywają.
Natomiast w przypadku parametrów z podpunktu "b" widać, że populacje niemal od razu maleją. Gatunek N2 wymiera już chwilę po rozpoczęciu symulacji, a populacja gatunku N1 maleje ale nie wymiera.

## Graph 3
Patrząc na Gradient zaprezentowany na wykresie, jesteśmy w stanie zauważyć, że niezależnie od początkowej populacji gatunku N1 najszybciej populacje obu gatunków maleją na samym początku (czyt. "leci od prawej do lewej").
