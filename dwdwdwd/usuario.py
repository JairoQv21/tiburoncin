from datetime import datetime

class Usuario:
    
    def __init__(self, id, username, password, first_name, last_name, telephone, created_at=None, modified_at=None):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.created_at = created_at or datetime.now()
        self.modified_at = modified_at or datetime.now()

    def __repr__(self):
        return (f"Usuario(id={self.id}, username={self.username}, first_name={self.first_name}, "
                f"last_name={self.last_name}, telephone={self.telephone}, created_at={self.created_at}, "
                f"modified_at={self.modified_at})")

if __name__ == '__main__':

    # Ejemplo de uso
    usuario = Usuario(
        id=1,
        username='JOESSJ',
        password='TiBURoNciNuAah!02',
        first_name='JOE',
        last_name='ARROYO',
        telephone='6969-6969'
    )

    print(usuario)

        
        