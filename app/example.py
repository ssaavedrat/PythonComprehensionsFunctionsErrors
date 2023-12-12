import main

# Al llamar main.data el módulo se ejecuta
# print("Data:",main.data)

# Una opción es encapsular la ejecución en una función run()
print('inicia ejecución main')
main.run()
print('termina ejecución main\n')

# Pero queremos que se ejecute en la linea de comandos tambien, necesitamos un entry point __name__ == "__main__"

# Ahora podemos llamar main.data()
print("Data:", main.data)