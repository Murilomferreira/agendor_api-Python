import requests 
import json
from datetime import date


class Deals:  
    """
    Deals Agendor
    ~~~~~~~~~~~~~~~~~~~~~

    - list_deals_of_person :  List deals of this person. | BR : lista os negócios de uma determinada pessoa.
    ~~~~~~~~~~~~~~~~~~~~

    - create_deal_for_person : Create a new deal for person. | BR : Cria um novo negócio para uma determinada pessoa.

    ~~~~~~~~~~~~~~~~~~~~

    - list_deals_of_organization:  List deals of this organization. |  BR : Lista os negócios de uma determianda organização.
    ~~~~~~~~~~~~~~~~~~~~
    
    - create_deal_for_organization : Create a new deal for organization. | BR : Crie um novo negócio para uma determinada organização.
    ~~~~~~~~~~~~~~~~~~~~

    - updtate_deal : Update a deal. | Atualiza um negócio.  
    ~~~~~~~~~~~~~~~~~~~~

    - get_deal : Get an specific deal by ID. | Pega um negócio específico pelo seu ID.
    ~~~~~~~~~~~~~~~~~~~~
    
    - update_deal_status : Win, lose or reopen a deal. | BR : Ganhe, perca ou reabra um negócio.
    ~~~~~~~~~~~~~~~~~~~~
    
    - update_deal_stage : Change a deal's funnel stage. | BR : Altere o estágio do funil de um negócio.
    ~~~~~~~~~~~~~~~~~~~~

    - list_deals : List and search for deals. | BR : Lista e procura todas os negócios. 
    ~~~~~~~~~~~~~~~~~~~~
    """
    
    data_atual= date.today().strftime('%Y-%m-%dT00:00:00Z')

    def list_deals_of_person(self, person_id, authorization_token) -> requests:
        """
        - Está função lista os negócios da pessoa informada pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """

        _url = 'https://api.agendor.com.br/v3/people/{}/deals'.format(person_id)
        response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()

    def create_deal_for_person(self, person_id, authorization_token, title:str, description:str = None, 
    end_time:str = data_atual, ranking:int = 0,start_time:str = data_atual, owner_user:int = 0, funnel:int = 0,
    deal_stage:int = 0, value:int = 0,allow_to_all_users:bool=True) -> requests:
        """
        - Cria um negócio para pessoa informada pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """

        _body = {
            "title": title,
            "dealStatusText": "ongoing",
            "description": description,
            "endTime": end_time,
            "products": [
            0
            ],
            "ranking": ranking,
            "startTime": start_time,
            "ownerUser": owner_user,
            "funnel": funnel,
            "dealStage": deal_stage,
            "value": value,
            "allowedUsers": [
            0
            ],
            "allowToAllUsers": allow_to_all_users
        }

        _body = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/people/{}/deals'.format(person_id) 
        response = requests.post(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()

    def list_deals_of_organization(self, organization_id, authorization_token):
        """
        - Está função lista os negócios de uma organização informada pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        _url = 'https://api.agendor.com.br/v3/organizations/{}/deals'.format(organization_id) 
        response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()

    def create_deal_for_organization(self, organization_id, authorization_token, title:str, description:str = None, 
    end_time:str = data_atual,ranking:int = 0,start_time:str = data_atual, owner_user:int = 0, funnel:int = 0,
    deal_stage:int = 0, value:int = 0, allow_to_all_users:bool=True) -> requests:
        """
        - Está função cria um negócio para uma organização informado pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        _body = {
            "title": title,
            "dealStatusText": "ongoing",
            "description": description,
            "endTime": end_time,
            "products": [
            0
            ],
            "ranking": ranking,
            "startTime": start_time,
            "ownerUser": owner_user,
            "funnel": funnel,
            "dealStage": deal_stage,
            "value": value,
            "allowedUsers": [
            0
            ],
            "allowToAllUsers": allow_to_all_users
        }
        
        _body = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/organizations/{}/deals'.format(organization_id) 
        response = requests.post(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()

    def updtate_deal(self, authorization_token, id:int, allow_to_all_users:bool = True, startTime = data_atual,
    description:str = None, value:int = 0, owner_user:int = 0) -> requests:
        """
        - Está função atualiza um determiando negócio informado pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        _body = {
            "value": value,
            "description": description,
            "startTime": startTime,
            "products": [
            0
            ],
            "ownerUser": owner_user,
            "allowedUsers": [
            0
            ],
            "allowToAllUsers": allow_to_all_users
            } 
        _body = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/deals/{}'.format(id)
        response = requests.put(_url, headers={'Authorization': "Token " + authorization_token}, data = _body)
        return response.json()

    def get_deal(self, id, authorization_token):
        """
        - Está função lista um determinado negócio pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        _url = 'https://api.agendor.com.br/v3/deals/{}'.format(id)
        response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()

    
    def update_deal_status(self, id, authorization_token, end_time:str = data_atual, owner_user:int = 0, 
    deal_status_text:str = 'ongoing'  ):
        """
        - Está função atualiza o status de um negócio pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        _body = {
            "dealStatusText": deal_status_text,
            "ownerUser": owner_user,
            "endTime": end_time
        }
        _url = 'https://api.agendor.com.br/v3/deals/{}/status'.format(id)
        response = requests.put(_url, headers={'Authorization': "Token " + authorization_token}, data = _body)
        return response.json()

        
    def update_deal_stage(self, id, authorization_token, deal_stage:int):
        """
        - Está função atuazlia o estado de um negócio pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        _body = {
            "dealStage": deal_stage 
        }

        _body = json.dumps(_body)
        
        _url  = 'https://api.agendor.com.br/v3/deals/{}/stage'.format(id)
        response = requests.put(_url, headers={'Authorization': "Token " + authorization_token}, data = _body)
        return response.json()

    def list_deals(self, authorization_token):
        """
        - Está função lista todos os negocios.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~
        """        
        _url  = 'https://api.agendor.com.br/v3/deals'
        response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()



