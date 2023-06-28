"""
File 1 of module 1
"""
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
print("---->",os.path.abspath('.'))
#print("aqui>",sys.path)
from src.module1.file2 import file2_func1

# Testing text
def file1_func1(a: int, b: int):
    """

    :param argumento1: str essa coisa faz alguma coisa
    :param argumento2: str essa coisa faz alguma outra coisa    
          
    :returns: A message (just for me, of course).
    
    
    ``parametros coisa1 : **str**``
            essa coisa faz alguma coisa
  
        

    <retorno>``alou`` não funciona
    
    .. figure:: /images/azul.jpg
       :alt: referenciaMaybe
       :scale: 40%
       :align: center
       
       *Legenda da imagem*
       
    .. warning::

       Warning!!! 
       
    .. note::

       Note!!! Admonições: attention, caution, danger, error, hint, important, note, tip, warning e a genérica admonition.   
       
    .. important::

       Important!!!      

    .. admonition:: Remember!

       #. That is the text that goes inside the box Remember
       #. Lista numerada
   
    coisa2 : int
       essa coisa serve pra alguma coisa
            
    Args:
        - a: int : integer to sum
        - b: int : integer to sum
        
    Returns:        
        - int: sum of the given values
        
    This is a normal text paragraph. The next paragraph is a code sample::

        It is not processed in any way, except
        that the indentation is removed.

        It can span multiple lines.
        # comentário? Sim

    This is a normal text paragraph again. 
    
    Grid Table:
        +------------------------+------------+----------+----------+
        | Header row, column 1   | Header 2   | Header 3 | Header 4 |
        | (header rows optional) |            |          |          |
        +========================+============+==========+==========+
        | body row 1, column 1   | column 2   | column 3 | column 4 |
        +------------------------+------------+----------+----------+
        | body row 2             | ...        | ...      |          |
        +------------------------+------------+----------+----------+   
    
    Simple Table:
        =====  =====  =======
        A      B      A and B
        =====  =====  =======
        False  False  False
        True   False  False
        False  True   False
        True   True   True
        =====  =====  =======
    """
    return a + b

def file1_func2(param1: str, param2: int, param3: bool):
    """"This function returns the 10 or the param2 times 3 if ...


    :param  param1: (str): String to check if we should do something.  
    :param    param2: (int): Base value to the multiplication.
    :param    param3: (bool): If we should do the multiplication or not.

    :returns: **int:** _description_
    """
    file2_func1()
    if param3 and param1 == "Y":
        return param2 * 3
    return 10

print(file1_func2("eita",3,True))