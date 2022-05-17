from datetime import *

"""
Graficos de juego
"""
def saltarconsola(cantidad):
    clearConsole = lambda: print('\n' * cantidad)
    clearConsole()
    print('─────────────────────█▄██▄█─────────────────────────\n'
          '────────────█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█────────────────\n'
          '────────────███┼█████▐████▌█████┼███────────────────\n'
          '────────────█████████▐████▌█████████────────────────\n'
          '█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n'
          '█ █   █ █▀▀█ █▀▀▄ █  █▀▀▄    █▀▀ █▀▀▄ █▀▀█ █▀▀ ▀█▀ █\n'
          '█ █▄█▄█ █  █ █▄▄▀ █  █  █    █   █▄▄▀ █▀▀█ █▀▀  █  █\n'
          '█  ▀ ▀  ▀▀▀▀ ▀  ▀ ▀▀ ▀▀▀     ▀▀▀ ▀  ▀ ▀  ▀ ▀    ▀  █\n'
          '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')


def texto(estado, tex1, tex2, tex3):
    if estado == 2:
        print('▄██████████████▄▐█▄▄▄▄█▌\n'
              f'██████▌▄▌▄▐▐▌███▌▀▀██▀▀  {tex1}\n'
              f'████▄█▌▄▌▄▐▐▌▀███▄▄█▌    {tex2}\n'
              f'▄▄▄▄▄██████████████▀     {tex3}')
    elif estado == 1:
        print('─────▀▄▀─────▄─────▄\n'
              '──▄███████▄──▀██▄██▀\n'
              f'▄█████▀█████▄──▄█    {tex1}.\n'
              f'███████▀████████▀    {tex2}\n'
              f'─▄▄▄▄▄▄███████▀      {tex3}')


def avatar(nombre, nivel, mundo):
    if nivel <= 20:
        print(f'             █▀▄     ▄▀█        Mundo: {mundo}\n'
              f'            █░ ▀▄▄▄▀ ░█\n'
              f'            █░       ░█         Nombre: {nombre} \n'
              f'      ▄▄    █  ░   ░  █         Nivel: {nivel}\n'
              f'      █░█   █  █   █  █\n'
              f'     █░░█   █    ▄▄   █\n'
              f'    █░░█  ▄▀░░░░▄░░▄░░░▀▄       Inventario: \n'
              f'    █░░█  ▀▀▄▄░░░▀▀░ ▄▄▀▀         Cuchillo\n'
              f'   ▀▀████▄▄▄▄▄█▀▀▀▀▀█▄     \n'
              f'     █▄▄▄▄▄▄▄▄▄     ▄▄▀▀▄▄▄\n'
              f'     █ █      █ ░░░ █ ▀▀█▄▄█\n'
              f'      ▀▀      █ ░░░ █      \n'
              f'             █  ▄▄▄ █▄     \n'
              f'           █▀ ▄▀   ▀▄ ▀█   \n'
              f'           ▀▀▀       ▀▀▀')
    elif 20 <= nivel <= 60:
        print(f'       ▄▄   █▀▄     ▄▀█         Mundo: {mundo}\n'
              f'      █░█   █░ ▀▄▄▄▀ ░█\n'
              f'     █░░█   █░       ░█         Nombre: {nombre} \n'
              f'    █░░█    █  ░   ░  █         Nivel: {nivel}\n'
              f'    █░░█    █  █   █  █\n'
              f'    █░░█    █    ▄▄   █\n'
              f'    █░░█  ▄▀░░░░▄░░▄░░░▀▄       Inventario: \n'
              f'    █░░█  ▀▀▄▄░░░▀▀░ ▄▄▀▀         Espada \n'
              f'   ▀▀████▄▄▄▄▄█▀▀▀▀▀█▄   \n'
              f'     █▄▄▄▄▄▄▄▄▄     ▄▄▀▀▄▄▄\n'
              f'     █ █      █ ░░░ █ ▀▀█▄▄█\n'
              f'      ▀▀      █ ░░░ █      \n'
              f'             █  ▄▄▄ █▄     \n'
              f'           █▀ ▄▀   ▀▄ ▀█    \n'
              f'           ▀▀▀       ▀▀▀')
    elif 60 <= nivel <= 100:
        print(f'       ▄▄   █▀▄     ▄▀█         Mundo: {mundo}\n'
              f'      █░█   █░ ▀▄▄▄▀ ░█\n'
              f'     █░░█   █░       ░█         Nombre: {nombre} \n'
              f'    █░░█    █  ░   ░  █         Nivel: {nivel}\n'
              f'    █░░█    █  █   █  █\n'
              f'    █░░█    █    ▄▄   █\n'
              f'    █░░█  ▄▀░░░░▄░░▄░░░▀▄  ▄▄\n'
              f'    █░░█  ▀▀▄▄░░░▀▀░ ▄▄▀▀  █▒█  Inventario: \n'
              f'   ▀▀████▄▄▄▄▄█▀▀▀▀▀█▄     █▒░█    Espada\n'
              f'     █▄▄▄▄▄▄▄▄▄     ▄▄▀▀▄▄▄█▒░░█   Escudo\n'
              f'     █ █      █ ░░░ █ ▀▀█▄▄█▒░░█\n'
              f'      ▀▀      █ ░░░ █      █▒░█\n'
              f'             █  ▄▄▄ █▄     █▒█\n'
              f'           █▀ ▄▀   ▀▄ ▀█    ▀\n'
              f'           ▀▀▀       ▀▀▀')

# ---------- Validaciones-------------
"""
Fin de graficos de juego
-----------------------------------------------------------------------
Validaciones de juego
"""
def validar_cdia(cdia):
    if len(cdia) == 10:
        mas = 0;
        k = 0;
        sinb = 0
        for cont in cdia:
            if cont == '+': mas += 1
            if cont == 'k': k += 1
            if cont == '?' or cont == '=' or cont == '&': sinb += 1
        if cdia.find('@') + 1 == 6 and cdia[0] != cdia[9] and mas >= 1 and k <= 3 and sinb >= 1:
            if not any(chr.isdigit() for chr in cdia):
                return True
    return False


def validar_inscritos(nuevo_jugador):
    nuevo_jugador = nuevo_jugador.swapcase()
    jugadores_all = {
        # 'qwertf@fgh': True,
        '+wert@ekk&': True,
        '+wert@ekk=': True,
        # 'qwert@efgh': True,
        # 'qwer1@efgh': True,
        # '+wert@ekkk': True,
    }
    jugadores_inscritos = {}

    for players in jugadores_all:
        if validar_cdia(players):
            jugadores_inscritos[players.swapcase()] = validar_cdia(players)

    for inscritos in jugadores_inscritos:
        if inscritos == nuevo_jugador:
            saltarconsola(100)
            return False
        else:
            return True
    # print(jugadores_inscritos)


def validar_edad(edad):
    edad_limpia = ''.join(filter(str.isalnum, edad))
    if len(edad) == 10 and edad_limpia.isdigit():
        fecha_nacimiento = datetime.strptime(edad, '%d/%m/%Y')
        hoy = datetime.today()
        annio = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if annio > 12:
            return annio
        else:
            saltarconsola(100)
            return 'menor'
    return False


def validar_alias(alias):
    cont_spacios = 0
    for espacios in alias:
        if espacios == ' ':
            cont_spacios = cont_spacios +1
    if len(alias) == 5 and alias.isalpha() and not cont_spacios >= 1:
        return True
    else:
        return False


def validar_preguntaSioNo(respuesta):
    if respuesta.swapcase() == 'SI':
        return True
    elif respuesta.swapcase() == 'NO':
        return False
    else:
       return False

"""
Fin de validaciones de juego
-----------------------------------------------------------------------
Logica del juego
"""
def validar_nivel(nivel):
    if nivel.isalpha():
        return False
    elif nivel:
        if int(nivel) > 1 or int(nivel) < 100:
            return True
    else:
        return False


def niveles_juego(edad,jugador_antiguo,nivel):
    print(type(edad), edad)
    if 12 < edad <= 20 and jugador_antiguo == False:
        return 'Mundo 1'
    elif 12 < edad <= 20 and jugador_antiguo == True and nivel < 50:
        return 'Mundo 2'
    elif 12 < edad <= 20 and jugador_antiguo == True and nivel > 50:
        return 'Mundo 3'
    elif edad >= 20 and jugador_antiguo == False:
        return 'Mundo 4'
    elif edad >= 20 and jugador_antiguo == True and nivel < 50:
        return 'Mundo 5'
    elif edad >= 20 and jugador_antiguo == True and nivel > 50:
        return 'Mundo 6'
    else:
        return 'Mundo magico'


def posicioamiento_niveles(edad,nievel_actual,jugador_antiguo):
    nievel = int(nievel_actual)
    if edad < 16:
        if not validar_preguntaSioNo(jugador_antiguo):
            return 2
        elif validar_preguntaSioNo(jugador_antiguo):
             return nievel

    if edad >= 16:
        if not validar_preguntaSioNo(jugador_antiguo):
            return 1
        elif validar_preguntaSioNo(jugador_antiguo):
            nuevo_nievel = nievel + 2
            if nuevo_nievel > 100:
                return 100
            else:
                return nuevo_nievel

#--------Main----------------------

"""
Fin de logica del juego
-----------------------------------------------------------------------
Main
"""
if __name__=='__main__':
      saltarconsola(1)
      print('Nuevo jugador. \nPorfavor crear un codigo CDIA.\n'
            'El CDIA debe contener los siguientes caracteres:\n'
            '1. Debe contener 10 caracteres\n'
            '2. No puede contener numeros.\n'
            '3. en sexto caracter debe ser un "@".\n'
            '4. debe contener un "+".\n'
            '5. No debe contener mas de 3 veces la letra "k"\n'
            '6. Debe tener almenos uno de estos simbolos (‘?’,’=’,’&’) \n'
            '7. El pimero y ultimo coracter deben ser diferentes\n')
      while True:
          cdia_jugador = input('Ejemplo ( w+ert@ekk& ):')
          if not validar_cdia(cdia_jugador):
              saltarconsola(100)
              texto(2, 'CDIA invalido.', 'Por favor,', 'ingresar CDIA valido')
          else:
              break
  
      saltarconsola(100)
      texto(1, 'Bievenido a World craft.',
            'Para continuar con el registro porfavor',
            'ingresa tu fecha de nacimiento (DD/MM/AAAA')
      while True:
          fecha_nacimiento = input('Fecha de nacimiento: ')
          if not validar_edad(fecha_nacimiento):
              saltarconsola(100)
              texto(2, 'Lo sentimos.', 'Formato de fecha invalido', '(DD/MM/AAA')
          elif validar_edad(fecha_nacimiento) == 'menor':
              saltarconsola(100)
              texto(2, 'Lo sentimos.', 'Debes ser mayor de 12 años', 'para jugar. Hasta luego')
              
          else: global annio; annio = validar_edad(fecha_nacimiento); break
  
      saltarconsola(100)
      texto(1, 'Es hora de colocarte un alias.', 'El alias debe:','Tener 5 caractere y No debe tener espacios en blnaco')
      while True:
          alias = input()
          if validar_alias(alias): break
          else:
              saltarconsola(100)
              texto(2, 'Lo sentimos.', 'El alias debe:',
                    'Tener 5 caractere y No debe tener espacios en blnaco')
  
      saltarconsola(100)
      texto(1, f'Hola. {alias}', '¿Ya has jugado WorldCraft antes?', '( Si o No ): ')
      while True:
          jugador_antiguo = input('Respuesta >>> ')
          if not validar_preguntaSioNo(jugador_antiguo):
              saltarconsola(100)
              texto(2, 'Lo sentimos, La respuesta no es valida.', '¿Ya has jugado WorldCraft antes?', '( Si o No )')
          else: break
  
      saltarconsola(100)
      texto(1, f'Hola. {alias}', '¿Hasta que nivel llegaste?', '(los niveles van desde 1 hasta 100): ')
      while True:
           nivel = input('Respuesta >>> ')
           if not validar_nivel(nivel):
               saltarconsola(100)
               texto(2, f'Hola. {alias}', '¿Hasta que nivel llegaste?', '(los niveles van desde 1 hasta 100): ')
           else: break
  
      saltarconsola(100)
      n_nivel = posicioamiento_niveles(annio, nivel, jugador_antiguo)
      mundo = niveles_juego(annio, True, n_nivel)
      saltarconsola(100)
      avatar(alias, n_nivel, mundo)
