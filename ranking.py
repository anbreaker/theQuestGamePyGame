
import sqlite3


class Ranking():
    # Constructor de la clase Menu
         
    
    def create_table(self,c):
        c.execute("CREATE TABLE IF NOT EXISTS `ranking` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `user` TEXT NOT NULL, `point` INTEGER NOT NULL)")
    
    def data_entry(self,c,conn):
        c.execute("INSERT INTO ranking (user, point) VALUES('probando',6)")
        conn.commit()
        c.close()
        conn.close()

    def mostrar_ranking(self):
        
        conn = sqlite3.connect('ranking.db')
        c = conn.cursor()
        
        self.create_table(c)
        self.data_entry(c,conn)
        
        
        
