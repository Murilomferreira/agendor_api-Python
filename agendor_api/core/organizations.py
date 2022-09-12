import requests
import json

class Organizations:
    """
    Organizations Agendor
    ~~~~~~~~~~~~~~~~~~~~

    - listOrganizations : List and search for organizations. |
    BR : Lista e procura todas organizações
    ~~~~~~~~~~~~~~~~~~~~

    - createOrganizarion : Create a new organization. | 
    BR : Crie uma nova organização.
    ~~~~~~~~~~~~~~~~~~~~

    - getOrganization: Get an specific organization by ID | 
    BR : Pegue uma organização específica pelo ID
    ~~~~~~~~~~~~~~~~~~~~
    
    - deleteOrganization : Delete an organization. |
    BR : Deletar uma organização
    ~~~~~~~~~~~~~~~~~~~~

    - updateOrganization : Update a specific organization by ID. |
    BR : Atualize uma organização específica pelo ID 
    ~~~~~~~~~~~~~~~~~~~~

    - upsertOrganization : If found, update it, otherwise, create a new one. 
    This endpoint is very useful if you want to avoid verifying for duplicates before creating a new organization. | BR:  Se encontrado, atualize-o, caso contrário, crie um novo. 
    Esse endpoint é muito útil se você deseja evitar a verificação de duplicatas antes de criar uma nova organização.
    ~~~~~~~~~~~~~~~~~~~~
    """

    def list_organizations(self, authorization_token:str) -> requests:
        """
        Listar Organizações
        ~~~~~~~~~~~~~~~~~~~~

        - Está função lista todas as organizações existentes.

        - Authorization_Token é encontrado na plataforma do agendor, 
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.

        - A funçao sempre retornara o valor do request em json. 

        """

        _url = 'https://api.agendor.com.br/v3/organizations'
        _response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return _response.json()
        

    def create_organizarion(self, authorization_token:str, name:str, legalName = None, cnpj = None, description = None,
    logo = None, website = None, ranking:int = None, ownerUser:int = None, email:str = None, work = None, mobile = None,
    fax = None , whatsapp = None, facebook = None, twitter = None, instagram = None, linked_in = None, skype = None, codigo_postal = None,
    pais = None, estado = None, uf = None, nome_rua = None, numero_casa:int = None, infromacao_adicional = None, cidade:int = None, allowToAllUsers:bool = None) -> requests: 
        """
        - Está função criara uma organização.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """

        _url = 'https://api.agendor.com.br/v3/organizations'

        _body =  {
                "name": name, 
                "legalName": legalName,
                "cnpj": cnpj,
                "description": description,
                "logo": logo,
                "website": website,
                "ranking": ranking,
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
                    "linked_in": linked_in,
                    "skype": skype 
                },
                "address": { 
                    "postal_code": codigo_postal, 
                    "country": pais, 
                    "district": estado,
                    "state": uf,
                    "street_name": nome_rua,
                    "street_number": numero_casa,
                    "additional_info": infromacao_adicional,
                    "city": cidade
                },
                "leadOrigin": 0,
                "category": 0,
                "sector": 0,
                "products": [
                0
                ],
                "allowedUsers": [
                0
                ],
                "allowToAllUsers": allowToAllUsers
            }

        _body = json.dumps(_body)
        response = requests.post(_url, headers={'Authorization': "Token " + authorization_token}, data=_body)
        return response.json()

    def get_organization(self, id:int, authorization_token:str) -> requests:
        """
        - Está função lista uma organização pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """

        _url= 'https://api.agendor.com.br/v3/organizations/{}'.format(id)
        response = requests.get(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()



    def delete_organization(self, id:int, authorization_token:str) -> requests:
        """
        - Está função deleta uma organização pelo seu  ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """

        _url = 'https://api.agendor.com.br/v3/organizations/{}'.format(id)
        response = requests.delete(_url, headers={'Authorization': "Token " + authorization_token})
        return response.json()

    def update_organization(self, id:int, authorization_token:str, name:str, legalName, cnpj, description, logo, website,
     ranking:int, ownerUser:int, email:str, work, mobile, fax , whatsapp, facebook, twitter, instagram, linked_in, skype,
      codigo_postal, pais, estado, uf, nome_rua, numero_casa:int, infromacao_adicional, cidade:int, allowToAllUsers:bool) -> requests:
        """
        - Está função atualiza uma organização pelo seu ID.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """
        
        _body =  {
                "name": name,
                "legalName": legalName,
                "cnpj": cnpj,
                "description": description,
                "logo": logo,
                "website": website,
                "ranking": ranking,
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
                    "linked_in": linked_in,
                    "skype": skype 
                },
                "address": { 
                    "postal_code": codigo_postal, 
                    "country": pais, 
                    "district": estado,
                    "state": uf,
                    "street_name": nome_rua,
                    "street_number": numero_casa,
                    "additional_info": infromacao_adicional,
                    "city": cidade
                },
                "leadOrigin": 0,
                "category": 0,
                "sector": 0,
                "products": [
                0
                ],
                "allowedUsers": [
                0
                ],
                "allowToAllUsers": allowToAllUsers
            }
        _body = json.dumps(_body)
        
        _url = 'https://api.agendor.com.br/v3/organizations/{}'.format(id)
        response = requests.put(_url, headers={'Authorization': "Token " + authorization_token}, data=_body)
        return response.json()

    def upsert_organization(self, authorization_token:str, name:str, legalName, cnpj, description, logo, website, ranking:int,
    ownerUser:int, email:str, work, mobile, fax , whatsapp, facebook, twitter, instagram, linked_in, skype, codigo_postal, pais,
    estado, uf, nome_rua, numero_casa:int, infromacao_adicional, cidade:int, allowToAllUsers:bool) -> requests:
        """
        - Está função se encontra uma organização então atualiza, se não, crie um novo.
         ~~~~~~~~~~~~~~~~~~~~

        - Authorization_Token é encontrado na plataforma do agendor
        exemplo : 12a34567-8912-3b45-c6de-f7g891h2i345.
         ~~~~~~~~~~~~~~~~~~~~

        - A funçao sempre retornara o valor do request em json. 
         ~~~~~~~~~~~~~~~~~~~~

        """ 
        _body =  {
            "name": name,
            "legalName": legalName,
            "cnpj": cnpj,
            "description": description,
            "logo": logo,
            "website": website,
            "ranking": ranking,
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
                "linked_in": linked_in,
                "skype": skype 
            },
            "address": { 
                "postal_code": codigo_postal, 
                "country": pais, 
                "district": estado,
                "state": uf,
                "street_name": nome_rua,
                "street_number": numero_casa,
                "additional_info": infromacao_adicional,
                "city": cidade
            },
            "leadOrigin": 0,
            "category": 0,
            "sector": 0,
            "products": [
            0
            ],
            "allowedUsers": [
            0
            ],
            "allowToAllUsers": allowToAllUsers
        }
        _body = json.dumps(_body)
        
        _url = 'https://api.agendor.com.br/v3/organizations/upsert'
        response = requests.post(_url, headers={'Authorization': "Token " + authorization_token}, data=_body)
        return response.json()