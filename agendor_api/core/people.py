import requests
import json

class People:
    """
        People Agendor
        ~~~~~~~~~~~~~~~

        - listPeople : List and search for people. |
        BR : Lista e procura todas pessoas
        ~~~~~~~~~~~~~~~~~~~~

        - createPerson : Create a new person. | 
        BR : Crie uma nova pessoa.
        ~~~~~~~~~~~~~~~~~~~~

        - getPerson: Get an specific person by ID. | 
        BR : Pegue uma pessoa específica pelo seu ID
        ~~~~~~~~~~~~~~~~~~~~
        
        - deletePerson : Delete a person. |
        BR : Deletar uma pessoa
        ~~~~~~~~~~~~~~~~~~~~

        - updatePerson : Update a specific person by ID. |
        BR : Atualize uma pessoa específica pelo seu ID 
        ~~~~~~~~~~~~~~~~~~~~

        - upsertOrganization : Search for a person by email.
        If found, update it, otherwise, create a new one.
        This endpoint is very useful if you want to avoid verifying for duplicates before creating a new person. |  
        BR : Procura uma pessoa pelo seu email. Se for encontrada então atualize, se não crie uma nova. 
        Esse endpoint é muito util quando você quiser evitar a verificação de duplicados antes de criar uma nova 
        pessoa. 
        ~~~~~~~~~~~~~~~~~~~~
        """

    def list_people(self, authorization_token:str) -> requests:
        """
        Listar Pessoas
        ~~~~~~~~~~~~~~~~~~~~

        - Está função lista todas as pessoas existentes.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """

        _url = 'https://api.agendor.com.br/v3/people'
        _response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return _response.json()
    
    def createPerson(self, authorization_token:str, name:str, uf:str,   cpf:str = None, organization:int = 0, role:str = None ,
    ranking:int = 0, description:str = None, ownerUser:int = 0, email:str = None, work:str = None, mobile:str = None,
    fax:str = None, whatsapp:str = None, facebook:str = None, twitter:str = None, instagram:str = None, linkedin:str = None,
    skype:str = None, postal_code:str = None, pais:str = None, estado:str = None,  rua:str = None, numero_casa:int = 0, 
    additional_info:str = None, cidade:int = 0, leadOrigin:int = 0, category:int = 0, allowToAllUsers:bool = True) -> requests:
        """
        Criar nova Pessoa
        ~~~~~~~~~~~~~~~~~~~~

        - Está função cria uma nova pessoa na base do Agendor.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """

        _body = {
                "name": name,
                "cpf": cpf,
                "organization": organization,
                "role": role,
                "ranking": ranking,
                "description": description,
                "birthday": None,
                "ownerUser": ownerUser,
                "contact": {
                    "email": email,
                    "work": work,
                    "mobile": mobile,
                    "fax": fax,
                    "whatsapp": whatsapp,
                    "facebook": facebook,
                    "twitter": twitter,
                    "instagram": instagram,
                    "linked_in": linkedin,
                    "skype": skype
                },
                "address": {
                    "postal_code": postal_code,
                    "country": pais,
                    "district": estado,
                    "state": uf,
                    "street_name": rua,
                    "street_number": numero_casa,
                    "additional_info": additional_info,
                    "city": cidade
                },
                "leadOrigin": leadOrigin,
                "category": category,
                "products": [
                0
                ],
                "allowedUsers": [
                0
                ],
                "allowToAllUsers": allowToAllUsers
            }
        _body  = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/people'
        _response = requests.post(_url, headers={'Authorization': "Token " + authorization_token}, data=_body)
        return _response.json()
    

    def get_person(self, id:int, authorization_token:str) -> requests:
        """
        listar pessoa pelo seu ID
        ~~~~~~~~~~~~~~~~~~~~

        - Está função tras os dados de uma determinada pessoa informanado o ID.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """

        _url = 'https://api.agendor.com.br/v3/people/{}'.format(id)
        _response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return _response.json()
   
    def delete_person(self, id:int, authorization_token:str) -> requests:
        """
        Deleta uma pessoa pelo seu ID
        ~~~~~~~~~~~~~~~~~~~~

        - Está função tras os dados de uma determinada pessoa informanado o ID.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """

        _url = 'https://api.agendor.com.br/v3/people/{}'.format(id)
        _response = requests.delete(_url, headers={'Authorization': "Token " + authorization_token})
        return _response.json()

    def update_person(self, authorization_token:str, name:str, uf:str,   cpf:str = None, organization:int = 0, role:str = None ,
    ranking:int = 0, description:str = None, ownerUser:int = 0, email:str = None, work:str = None, mobile:str = None,
    fax:str = None, whatsapp:str = None, facebook:str = None, twitter:str = None, instagram:str = None, linkedin:str = None,
    skype:str = None, postal_code:str = None, pais:str = None, estado:str = None,  rua:str = None, numero_casa:int = 0, 
    additional_info:str = None, cidade:int = 0, leadOrigin:int = 0, category:int = 0, allowToAllUsers:bool = True) -> requests:
        """
        Atualiza uma  pessoa específica pelo seu ID
        ~~~~~~~~~~~~~~~~~~~~

        - Está função tras os dados de uma determinada pessoa informanado o ID.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """
        _body = {
                "name": name,
                "cpf": cpf,
                "organization": organization,
                "role": role,
                "ranking": ranking,
                "description": description,
                "birthday": None,
                "ownerUser": ownerUser,
                "contact": {
                    "email": email,
                    "work": work,
                    "mobile": mobile,
                    "fax": fax,
                    "whatsapp": whatsapp,
                    "facebook": facebook,
                    "twitter": twitter,
                    "instagram": instagram,
                    "linked_in": linkedin,
                    "skype": skype
                },
                "address": {
                    "postal_code": postal_code,
                    "country": pais,
                    "district": estado,
                    "state": uf,
                    "street_name": rua,
                    "street_number": numero_casa,
                    "additional_info": additional_info,
                    "city": cidade
                },
                "leadOrigin": leadOrigin,
                "category": category,
                "products": [
                0
                ],
                "allowedUsers": [
                0
                ],
                "allowToAllUsers": allowToAllUsers
            }

        _body = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/people/{}'.format(id) 
        _response = requests.put(_url, headers={'Authorization': "Token " + authorization_token}, data = _body)
        return _response.json()

    def upsert_person(self, authorization_token:str, name:str, uf:str,   cpf:str = None, organization:int = 0, role:str = None ,
    ranking:int = 0, description:str = None, ownerUser:int = 0, email:str = None, work:str = None, mobile:str = None,
    fax:str = None, whatsapp:str = None, facebook:str = None, twitter:str = None, instagram:str = None, linkedin:str = None,
    skype:str = None, postal_code:str = None, pais:str = None, estado:str = None,  rua:str = None, numero_casa:int = 0, 
    additional_info:str = None, cidade:int = 0, leadOrigin:int = 0, category:int = 0, allowToAllUsers:bool = True) -> requests:
        """
        Pesquisa uma pessoa pelo seu Email, se for encontrada então atualize,  se não crie uma nova. 
        ~~~~~~~~~~~~~~~~~~~~

        - Está função tras os dados de uma determinada pessoa informanado o ID.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """
        _body = {
                "name": name,
                "cpf": cpf,
                "organization": organization,
                "role": role,
                "ranking": ranking,
                "description": description,
                "birthday": None,
                "ownerUser": ownerUser,
                "contact": {
                    "email": email,
                    "work": work,
                    "mobile": mobile,
                    "fax": fax,
                    "whatsapp": whatsapp,
                    "facebook": facebook,
                    "twitter": twitter,
                    "instagram": instagram,
                    "linked_in": linkedin,
                    "skype": skype
                },
                "address": {
                    "postal_code": postal_code,
                    "country": pais,
                    "district": estado,
                    "state": uf,
                    "street_name": rua,
                    "street_number": numero_casa,
                    "additional_info": additional_info,
                    "city": cidade
                },
                "leadOrigin": leadOrigin,
                "category": category,
                "products": [
                0
                ],
                "allowedUsers": [
                0
                ],
                "allowToAllUsers": allowToAllUsers
            }
        _body = json.dumps(_body)
        _url = 'https://api.agendor.com.br/v3/people/upsert'
        response = requests.post(_url, headers={'Authorization': "Token " + authorization_token}, data=_body)
        return response.json()

    def list_people_of_organization(self, organization_id:int, authorization_token:str) -> requests:
        """
        Lista todas as pessoas de uma organização. 
        ~~~~~~~~~~~~~~~~~~~~

        - Está função tras os dados de uma determinada pessoa informanado o ID.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """
        _url = 'https://api.agendor.com.br/v3/organizations/{}/people'.format(organization_id)
        response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()