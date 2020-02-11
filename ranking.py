
import sqlite3


class Ranking():
    # Constructor de la clase Menu
    # Para implementar las llamadas a la BBDD
    # ranking = Ranking()
    # ranking.mostrar_ranking()
    
    
    '''
    1.- Control de errores
    Cuando hagáis accesos a la base de datos deberéis controlar el error en acceso 
    a datos (por ejemplo inserciones con clave duplicada) o bloqueo de la base de 
    datos porque estéis haciendo inserciones desd SQLite Browser. La forma ya la conocéis.
    try:
        dbQuery(consulta, parametros)
        except sqlite3.Error as e:
    <procesar error>
    Este <procesar error> puede ser:
    form.errors['general'] = ['Error en acceso a base de datos: {}'.format(e)]
    return render_template('vuestro.html', form)
    
    En pygame, mostrar un error bien en la consola (terminal)
    lblError.config(text='Errorn en acceso a base de datos: {}'.format(e)) 
    #algo así en tkinter siempre que lblError sea una label que muestra los errores o usando messagebox
    print('Error en acceso a base de datos: {}'.format(e))
    #algo así en pygame. A no ser que queráis mostrarlo en la propia pantalla del juego    
    '''
    
    def create_table(self,c):
        c.execute("CREATE TABLE IF NOT EXISTS `ranking` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `user` TEXT NOT NULL, `point` INTEGER NOT NULL)")
    
    def data_entry(self,c,conn):
        c.execute("INSERT INTO ranking (user, point) VALUES('SJA',650)")
        conn.commit()
        c.close()
        conn.close()

    def mostrar_ranking(self):
        
        conn = sqlite3.connect('ranking.db')
        c = conn.cursor()
        
        self.create_table(c)
        self.data_entry(c,conn)
        
        
        
