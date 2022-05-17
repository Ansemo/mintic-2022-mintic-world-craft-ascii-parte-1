# WORLD CRAFT ASCII: PARTE 1
![1](https://user-images.githubusercontent.com/104838545/168876197-abd51d6d-b848-41ef-b724-cf27ab306aa1.png)<br>
![3](https://user-images.githubusercontent.com/104838545/168876198-1675789a-3457-4cb9-ae43-2d43190a6101.png)<br>
![5](https://user-images.githubusercontent.com/104838545/168876201-6531478e-39be-41b6-b447-87e98a288209.png)<br>
![7](https://user-images.githubusercontent.com/104838545/168876202-95505484-3eac-4aeb-ab08-977b67be10a8.png)<br>
![8](https://user-images.githubusercontent.com/104838545/168876203-39b360ef-d96a-4372-8d9b-bc624c1bcf4f.png)<br>
![9](https://user-images.githubusercontent.com/104838545/168876204-f5bff69c-d117-4aa9-bb4d-d5a918f03ac6.png)<br>


<h1>RETO1: INGRESANDO AL JUEGO</h1>
Este primer reto se trata de implementar un programa que
permita verificar los datos de un aspirante a jugador del juego y
asignarle un nivel de inicio.
<h2>PRIMER SUB RETO: INSCRIPCIÓN DEL JUGADOR</h2>
Esta función tiene como objetivo realizar una verificación para
evaluar la posibilidad de que una persona pueda ingresar como
nuevo jugador del WorldCraft ASCII, para ello se solicita el CDIA
(código de identificación ASCII) del aspirante. Este CDIA es una
cadena de 10 caracteres que debe cumplir con las siguientes
restricciones y las cuales deben ser validadas por el programa una
vez se ingresa:
• Se debe verificar que el CDIA sea de tipo str exclusivamente y<br>
sin dígitos numéricos
• En la posición 6 de la cadena del CDIA debe ir siempre el<br>
carácter arroba (‘@’)
• El carácter en la primera posición y el carácter en la última<br>
posición del CDIA deben ser diferentes.
• El CDIA debe contener en cualquier posición de la cadena el<br>
carácter arroba (‘+’)
• El código CDIA no debe contener más de 3 veces la letra ’k’<br>
• El CDIA debe tener al menos uno de los siguientes símbolos<br>
(‘?’,’=’,’&’)
Si el CDIA no cumple con alguna de estas reglas se debe presentar
el mensaje “CDIA inválido”
Adicionalmente, el administrador del juego ha proporcionado una
lista con los códigos CDIA de todos los jugadores registrados de
WorldCraft ASCII, y tu formador ha desarrollado una función en
Python para que la utilices en la búsqueda de un código CDIA. Así
que: una vez validado el CDIA (es decir que cumpla las reglas
definidas), debes verificar que ya no se encuentre inscrito un
jugador con ese CDIA. Es importante tener en cuenta tambien que
antes de utilizar la función de búsqueda debes convertir todos los
caracteres del código CDIA que sean letras minúsculas a
mayúsculas.
A continuación, se presenta un ejemplo del uso de la función de
búsqueda de un CDIA.
<h2>SEGUNDO SUB-RETO: ASIGNAR MUNDO</h2>
Cuando un nuevo jugador es admitido al WorldCraft ASCII se le
debe asignar un Mundo para iniciar a jugar de acuerdo a las
siguientes reglas:
• Mundo 1: jugadores entre 12 y 20 años que no han jugado antes.<br>
• Mundo 2: jugadores entre 12 y 20 años que ya han jugado antes<br>
y su nivel actual es menor a 50.
• Mundo 3: jugadores entre 12 y 20 años que ya han jugado antes<br>
y su nivel actual es mayor o igual a 50.
• Mundo 4: jugadores mayores a 20 años que no han jugado antes<br>
• Mundo 5: jugadores mayores a 20 años que ya han jugado antes<br>
y su nivel actual es menor a 50.
• Mundo 5: jugadores mayores a 20 años que ya han jugado antes<br>
y su nivel actual es mayor o igual a 50.
Si la edad del jugador es mayor o igual a 16 años y ya ha jugado
antes debe ser enviado al nivel que tenía antes más 2, si no había
jugado antes debe ser enviado al nivel 1.
NOTA: tenga en cuenta que la edad del jugador no se debe solicitar
directamente pero si su fecha de nacimiento.
El programa debe tener una función que reciba la edad (ya
calculada) del nuevo jugador, la respuesta si ha jugado antes y su
nivel, con estos datos debe retornar el mundo que le corresponde al
jugador. 
