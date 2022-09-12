from datetime import date, datetime
import json
from sqlite3 import Timestamp
import requests

class Tasks:
    """
    Organizations Agendor
    ~~~~~~~~~~~~~~~~~~~~~

    - list_tasks_of_person : List and search for person. |
    BR : Lista e procura tarefa de uma pessoa
    ~~~~~~~~~~~~~~~~~~~~

    - create_task_for_person : Create a new task related to this person. | 
    BR : Crie uma nova tarefa relacionada a essa pessoa.
    ~~~~~~~~~~~~~~~~~~~~

    - list_tasks_of_organization: List and search tasks of an organization. | 
    BR : Listar e pesquisar tarefas de uma organização.
    ~~~~~~~~~~~~~~~~~~~~
    
    - create_task_for_organization : Create a new task related to this organization. |
    BR : Crie uma nova tarefa relacionada a esta organização.
    ~~~~~~~~~~~~~~~~~~~~

    - list_tasks_of_deal : List and search tasks of a deal. |
    BR : Listar e pesquisar tarefas de um negócio.
    ~~~~~~~~~~~~~~~~~~~~

    - create_task_for_deal : Create a new task related to this deal. | BR: Crie uma nova tarefa relacionada a este negócio.
    ~~~~~~~~~~~~~~~~~~~~

    - list_tasks : List and search tasks.  | BR: lista e procura todas as tarefas 
    ~~~~~~~~~~~~~~~~~~~~
    """

    def list_tasks_of_person(self, person_id:int, authorization_token:str ) -> requests:
        """
        lista as tarefas da pessoa
        ~~~~~~~~~~~~~~~~~~~~

        - Está função lista todas as tarefas existentes.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """ 

        _url = 'https://api.agendor.com.br/v3/people/{}/tasks'.format(person_id)
        _response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return _response.json()

    def create_task_for_person(self, organization_id:int, authorization_token:str, text:str, type:str = None,
    finished_by:int = 0 , finished_date:str = None, due_date:str = None) -> requests:
        """
        Cria uma nova tarefa para uma determinada pessoa
        ~~~~~~~~~~~~~~~~~~~~

        - Está função cria uma tarefa.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """ 

        _body = {
                "text": text,
                "assigned_users": [
                    0
                ],
                "due_date": due_date,
                "finished_date": finished_date,
                "finished_by": finished_by,
                "type": type,
                "metrics": [
                0
            ]
            }
        _body = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/people/{}/tasks'.format(person_id)
        _response = requests.post(_url, headers={'Authorization': "Token " + authorization_token}, data = _body)
        return _response.json()


    def list_tasks_of_organization(self, organization_id:int, authorization_token:int ) -> requests:
        """
        Lista as tarefas de uma organização
        ~~~~~~~~~~~~~~~~~~~~

        - Está função lista todas as tarefas existentes de uma organização.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """

        _url = 'https://api.agendor.com.br/v3/organizations/{}/tasks'.format(organization_id)
        _response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return _response.json()

 
    def  create_task_for_organization(self, organization_id:int, authorization_token:str, text:str, type:str = None,
    finished_by:int = 0 , finished_date:str = None, due_date:str = None) -> requests:
        """
        Crie uma nova tarefa para uma organização
        ~~~~~~~~~~~~~~~~~~~~

        - Está função cria uma tarefa para a organização determinada.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """
        _body = {
                "text": text,
                "assigned_users": [
                    0
                ],
                "due_date": due_date,
                "finished_date": finished_date,
                "finished_by": finished_by,
                "type": type,
                "metrics": [
                0
            ]
            }
        _body  = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/organizations/{}/tasks'.format(organization_id)
        _response = requests.post(_url, headers={'Authorization': "Token " + authorization_token}, data=_body)
        return _response.json()

    def list_tasks_of_deal(self, deal_id:int, authorization_token:str) -> requests:
        """
        Lista todas tarefas por um determinado acordo
        ~~~~~~~~~~~~~~~~~~~~

        - Está função lista uma tarefa por um determiando acordo 

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """

        _url = 'https://api.agendor.com.br/v3/deals/{}/tasks'.format(deal_id)
        _response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return _response.json()

    def create_task_for_deal(self, deal_id:int, authorization_token:str, text:str, type:str = None,
    finished_by:int = 0 , finished_date:str = None, due_date:str = None) -> requests:
        """
        cria uma tarefa para um acordo
        ~~~~~~~~~~~~~~~~~~~~

        - Está função cria uma tarefa por um determiando acordo 

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """
        _body = {
                "text": text,
                "assigned_users": [
                    0
                ],
                "due_date": due_date,
                "finished_date": finished_date,
                "finished_by": finished_by,
                "type": type,
                "metrics": [
                0
            ]
            }
        _body  = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/deals/{}/tasks'.format(deal_id)
        _response = requests.post(_url, headers={'Authorization': "Token " + authorization_token}, data = _body)
        return _response.json() 

    def list_tasks(self, authorization_token:str) -> requests:
        """
        lista todas tarefas de um acordo
        ~~~~~~~~~~~~~~~~~~~~

        - Está função lista todas as tarefas de um acordo

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """
        _url = 'https://api.agendor.com.br/v3/tasks'
        _response = requests.post(_url, headers={'Authorization': "Token " + authorization_token})
        return _response.json() 
