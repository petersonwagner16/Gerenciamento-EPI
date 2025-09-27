

# Projeto de Gerenciamento de EPIs

Este é um sistema web desenvolvido em Django para gerenciar o controle de Equipamentos de Proteção Individual (EPIs), usuários, empréstimos, devoluções e informações de colaboradores.

---


---

##  Principais Funcionalidades

* **Registrar dados**: Permite registrar informações em todas as tabelas do sistema.
* **Listar dados**: Exibe uma lista de todos os registros (colaboradores, equipamentos, empréstimos).
* **Atualizar dados**: Permite a edição de registros existentes.
* **Excluir dados**: Possibilita a remoção de registros.


---

###  Como executar o projeto

Para rodar este projeto em sua máquina local, siga os passos abaixo.

####  Requisitos

Certifique-se de que os seguintes programas estão instalados em seu computador:

* **Python 3.10+**
* **Git**
* **Pip**
* (Opcional) **Virtualenv**

### ✅ 1. Clone o repositório

Abra o seu terminal (Git Bash, PowerShell, etc.) e clone o projeto do GitHub.   



```bash
git clone (https://github.com/petersonwagner16/Gerenciamento-EPI.git)

```

✅ 2. Crie e ative o ambiente virtual
É uma boa prática isolar as dependências do projeto em um ambiente virtual.

```Bash

# Para Windows
python -m venv venv
.\venv\Scripts\activate


# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
✅ 3. Instale o django
Com o ambiente virtual ativado, instale o Django com o comando abaixo.

```Bash

pip install django
```


✅ 4. Inicie o servidor
Agora, você pode iniciar o servidor de desenvolvimento do Django.

```Bash

python manage.py runserver
```
O projeto estará acessível em seu navegador no seguinte endereço:

http://127.0.0.1:8000/
