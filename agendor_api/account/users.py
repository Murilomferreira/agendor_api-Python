import requests
import json

class Users:
    """
    Users Agendor
    ~~~~~~~~~~~~~

    - list_users :  List and search users of your account. | BR: Lista e procura todos os usuários de sua conta.
    ~~~~~~~~~~~~~

    - get_current_user : Get information about the authenticated user. | BR : Pega a informação sobre o usuário autenticado. 
    ~~~~~~~~~~~~~~~~~~~~
 
    - update_user : Activate or inactivate a specific user. | BR : Ative ou desative um usuário específico. 
    ~~~~~~~~~~~~~~

    """
    def list_users(self, authorization_token) -> requests:
        """
        - Está função lista todos os usuários desta conta.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """

        _url = 'https://api.agendor.com.br/v3/users'
        response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()

    def get_current_user(self, authorization_token) -> requests: 
        """
        - Está função pega o usuário atual.  
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        _url = 'https://api.agendor.com.br/v3/users/me'
        response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()
    
    def update_user(self, authorization_token:str, id:int, active:bool) -> requests:
        """
        - Está função atualiza um determinado usuário pelo seu ID:
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        _body = {

            "active": active
        }
        
        _body = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/users/{}'.format(id)
        response = requests.put(_url, headers={'Authorization': "Token " + authorization_token}, data = _body)
        return response.json()