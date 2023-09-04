from tienda import *
t= Tienda()
t.agragar_animal(Perro("boxer", 2 ,5))
t.agragar_animal(Perro("chiguaga", 2 ,1))
t.agragar_animal(Gato("angora", 2 ,0.5))
t.agragar_animal(Gato("persa", 2 ,0.7))
t.agragar_animal(Gato("criollo", 12 ,3.5))
t.agragar_animal(Pez("golden", 0.5 ,0.01))
t.agragar_animal(Pez("telescopio", 0.5 ,0.01))
t.agragar_animal(Pez("coridora", 0.5 ,0.01))
t.agragar_animal(Ave("loro", 1 ,0.5))
t.agragar_animal(Ave("perico", 1 ,0.5))
t.agragar_animal(Ave("cactuas", 1 ,0.5))

for i in range(5):
    a= t.entragar_animal()
    print(a.saludar(), a.mostrar_informacion())