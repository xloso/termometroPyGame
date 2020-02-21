import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("imagenes/termo1.png")
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados-32) * 5/9
        else:
            resultado = grados
            
        return "{:10.2f}".format(resultado)
        
class Selector():
    #atributo
    __tipoUnidad = 'C'
    
    #metodo es hacer click, el cambio de F a C o C a F
    def __init__(self, unidad="C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("imagenes/puntof.png"))
        self.__customes.append(pygame.image.load("imagenes/puntoc.png"))
        
        self.__tipoUnidad = unidad
        
    def custome(self):
        if self.__tipoUnidad == "F":
            return self.__customes[0]
        else:
            return self.__customes[1]
    
    def change(self):
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad == 'C'
        else:
            self.__tipoUnidad = 'F'
            
    #getter, simplemente devuelve el tipo de unidad.
    def unidad(self):
        return self.__tipoUnidad
                


class NumberInput():
    #atributos
    __value = 0
    __strValue = ""
    __position = [0, 0]
    __size = [0,0]
    __pointsCount = 0
    
    def __init__(self, value = 0):
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value)

        '''
            el self.value(value) hace lo mismo que lo de
            aquí abajo. Por eso invoco ese método para no repetirme
        try:
            self.__strValue = int(value)
            #como ya sabemos que es un entero, lo dejamos en string otra vez
            self.__strValue = str(value)
        except:
            pass
        '''
        
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode in '0123456789' and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount ==0):
                
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == '.':
                    self.__pointsCount +=1
                 
            elif event.key == K_BACKSPACE:
                if self.__strValue[-1] == '.':
                    self.__points -= 1
                self.__strValue = self.__strValue[:-1]
                self.value(self.__strValue)             
                
    def render(self):
        
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        #renderizar el rectangulo. 
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)
    
        '''
        esto devuelve los 2 valores en un diccionario otra opcion
        return {
                 "fondo": rect,
                 "tecto": textBlock
             }
        '''
    # definir setter y getter

    def value(self, val=None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = float(val)
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass
            
    #ahora setter y getter de la posicion
            
    def size (self, val = None):
          if val == None:
              return self.__size
          else:
              try:
                  self.__size = [int(val[0]), int(val[1])]
              except:
                  pass
                
    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
    
    def pos (self, val = None):
          if val == None:
              return self.__position
          else:
              try:
                  self.__position = [int(val[0]), int(val[1])]
              except:
                  pass
                  
class mainApp():
    #crear atributos
    termometro = None
    entrada = None
    selector = None
    
    #ahora el constructor, la pantalla
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236, 203))
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106, 58))
        self.entrada.size((133,28))
        
        self.selector = Selector()
        
    def __on_close(self):
        pygame.quit()
        sys.exit
        
    def start(self):
        #capturar eventos
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                
            #pintamos fondo pantalla
            self.__screen.fill((244, 236, 203))
                            
            #ahora pintar, renderizar el termometro en su posicion
            self.__screen.blit(self.termometro.custome, (50,34))
            
            #pintamos el cuadro de texto
            text = self.entrada.render() #obtenemos rectangulo blanco y foto de texto y lo asignamos a la variable text
            # pintamos, creamos el rectangulo blanco con sus datos, posicion y tamaño
            pygame.draw.rect(self.__screen, (255,255,255), text[0])
            # "pinto" el texto, pongo la foto del texto.
            self.__screen.blit(text[1], self.entrada.pos())
            
            #pintamos el selector
            self.__screen.blit(self.selector.custome(), (112,153))
            
            pygame.display.flip()
        
        
if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.start()
    