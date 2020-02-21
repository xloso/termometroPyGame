import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("imagenes/termo1.png")
        
class NumberInput():
    #atributos
    __value = 0
    __strValue = "0"
    __position = [0, 0]
    __size = [0,0]
    
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
            if event.unicode in '0123456789':
                
    
    def render (self):
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
                self.__value = int(val)
                self.__strValue = val
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
                            
            #ahora pintar, renderizar el termometro en su posicion
            self.__screen.blit(self.termometro.custome, (50,34))
            
            #pintamos el cuadro de texto
            text = self.entrada.render() #obtenemos rectangulo blanco y foto de texto y lo asignamos a la variable text
            # pintamos, creamos el rectangulo blanco con sus datos, posicion y tamaño
            pygame.draw.rect(self.__screen, (255,255,255), text[0])
            # "pinto" el texto, pongo la foto del texto.
            self.__screen.blit(text[1], self.entrada.pos())
            
            pygame.display.flip()
        
        
if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.start()
    