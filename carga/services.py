from .dictionaries import projects_dict_letter, agents_dict
from .models import Project, Agent
from .utils import parse_location


class Service:

    @staticmethod
    def fill_agent_dict(worksheet):
        localizacao = True
        nome = True
        for row in worksheet.iter_rows(min_row=5, max_col=76, max_row=5):
            for cell in row:
                print(cell.value)
                check_column = cell.value in agents_dict
                if check_column:
                    if cell.value == 'Localiza瀣o' and localizacao:
                        agents_dict[cell.value] = cell.col_idx
                        localizacao = False
                    elif cell.value == 'Nome' and nome:
                        agents_dict[cell.value] = cell.col_idx
                        nome = False
                    elif cell.value != 'Localiza瀣o' and cell.value != 'Nome':
                        agents_dict[cell.value] = cell.col_idx
                    else:
                        pass
        return agents_dict

    @staticmethod
    def parse_projects(worksheet):
        projects = []
        for row in worksheet.iter_rows(min_row=6, max_col=26, max_row=worksheet.max_row):
            project = Project()
            for cell in row:
                check_column = cell.column in projects_dict_letter
                if check_column:
                    if cell.column == "A":
                        project.code = cell.value
                    elif cell.column == "B":
                        project.name = cell.value
                    elif cell.column == "C":
                        project.description_short = cell.value
                    elif cell.column == "D":
                        project.description_long = cell.value
                    elif cell.column == "E":
                        if cell.value is not None:
                            project.last_update = cell.value
                    elif cell.column == "F":
                        if cell.value is not None:
                            project.registration_from = cell.value
                    elif cell.column == "G":
                        if cell.value is not None:
                            project.registration_to = cell.value
                    elif cell.column == "H":
                        if cell.value is not None:
                            project.created_at = cell.value
                    elif cell.column == "I":
                        project.parent_entity = cell.value
                    elif cell.column == "J":
                        project.published_by = cell.value
                    elif cell.column == "K":
                        project.project_budget = cell.value
                    elif cell.column == "L":
                        project.project_goal = cell.value
                    elif cell.column == "M":
                        project.target_audience = cell.value
                    elif cell.column == "O":
                        project.areas = cell.value
                    elif cell.column == "P":
                        project.tags = cell.value
                    elif cell.column == "Q":
                        project.verified_account = cell.value
                    elif cell.column == "R":
                        project.project_type = cell.value
                    elif cell.column == "S":
                        project.project_website = cell.value
                    elif cell.column == "T":
                        project.project_facebook = cell.value
                    elif cell.column == "U":
                        project.project_twitter = cell.value
                    elif cell.column == "V":
                        project.project_google_plus = cell.value
                    elif cell.column == "W":
                        project.project_instagram = cell.value
                    elif cell.column == "X":
                        project.stamps = cell.value
                    elif cell.column == "Y":
                        project.opportunity_tab_name = cell.value
                    elif cell.column == "Z":
                        project.uses_opportunity_tab = cell.value
            projects.append(project)
        return projects

    @staticmethod
    def parse_agent(worksheet, agents_col):
        agents = []
        for row in worksheet.iter_rows(min_row=6, max_col=76, max_row=worksheet.max_row):
            agent = Agent()
            for cell in row:
                if cell.col_idx == agents_col['Id']:
                    agent.agent_identifier = cell.value
                elif cell.col_idx == agents_col['Nome']:
                    agent.name = cell.value
                elif cell.col_idx == agents_col['Localiza瀣o']:
                    agent.latitude, agent.longitude = parse_location(cell.value)
                elif cell.col_idx == agents_col['Descri瀣o Curta']:
                    agent.description_short = cell.value
                elif cell.col_idx == agents_col['Descri瀣o Longa']:
                    agent.description_long = cell.value
                elif cell.col_idx == agents_col['Data de Cria瀣o']:
                    agent.created_at = cell.value
                elif cell.col_idx == agents_col['Data de Atualiza瀣o']:
                    agent.updated_at = cell.value
                elif cell.col_idx == agents_col['Entidade pai']:
                    agent.parent_entity = cell.value
                elif cell.col_idx == agents_col['Email Pblico']:
                    agent.public_email = cell.value
                elif cell.col_idx == agents_col['Telefone']:
                    agent.phone = cell.value
                elif cell.col_idx == agents_col['Endere瀯']:
                    agent.address = cell.value
                elif cell.col_idx == agents_col['CEP']:
                    agent.zip_code = cell.value
                elif cell.col_idx == agents_col['Estado']:
                    agent.state = cell.value
                elif cell.col_idx == agents_col['Munic퀰io']:
                    agent.city = cell.value
                elif cell.col_idx == agents_col['Bairro']:
                    agent.neighbourhood = cell.value
                elif cell.col_idx == agents_col['Logradouro']:
                    agent.public_place = cell.value
                elif cell.col_idx == agents_col['Nmero']:
                    agent.address_number = cell.value
                elif cell.col_idx == agents_col['Complemento']:
                    agent.address_other_info = cell.value
                elif cell.col_idx == agents_col['@reas']:
                    agent.fields_of_art = cell.value
                elif cell.col_idx == agents_col['Tags']:
                    agent.tags = cell.value
                elif cell.col_idx == agents_col['Verificado']:
                    agent.verified_account = cell.value
                elif cell.col_idx == agents_col['Tipo']:
                    agent.account_type = cell.value
                elif cell.col_idx == agents_col['Informe seu Nome Social']:
                    agent.social_name = cell.value
                elif cell.col_idx == agents_col['Informe seu Nome Profissional']:
                    agent.work_name = cell.value
                elif cell.col_idx == agents_col['Data de Nascimento']:
                    agent.date_of_birth = cell.value
                elif cell.col_idx == agents_col['Gꀮero']:
                    agent.gender = cell.value
                elif cell.col_idx == agents_col["Ra瀡/cor"]:
                    agent.ethnic_type = cell.value
                elif cell.col_idx == agents_col["Informe sua Orienta瀣o Sexual"]:
                    agent.sexual_orientation = cell.value
                elif cell.col_idx == agents_col["Informe seu Estado Civil"]:
                    agent.civil_status = cell.value
                elif cell.col_idx == agents_col["Informe sua Escolaridade"]:
                    agent.studies = cell.value
                elif cell.col_idx == agents_col["CPF"]:
                    agent.cpf = cell.value
                elif cell.col_idx == agents_col["Informe sua Identidade (RG)"]:
                    agent.rg = cell.value
                elif cell.col_idx == agents_col["Informe a Data de Expedi瀣o (RG)"]:
                    agent.rg_date = cell.value
                elif cell.col_idx == agents_col["Informe o Ӏrg〯 Expedidor (RG)"]:
                    agent.rg_orgao_expedidor = cell.value
                elif cell.col_idx == agents_col["Informe sua Nacionalidade"]:
                    agent.nationality = cell.value
                elif cell.col_idx == agents_col["Informe sua Naturalidade"]:
                    agent.natural_from = cell.value
                elif cell.col_idx == agents_col["Vocꀠ造uma pessoa com deficiꀮcia?"]:
                    if cell.value.__str__().strip == "":
                        agent.has_disability = False
                    else:
                        agent.has_disability = cell.value
                elif cell.col_idx == agents_col["Em caso de resposta afirmativa, que tipo de deficiꀮcia?"]:
                    agent.disability = cell.value
                elif cell.col_idx == agents_col["Email Principal"]:
                    agent.main_email = cell.value
                elif cell.col_idx == agents_col["Celular"]:
                    agent.cell_phone = cell.value
                elif cell.col_idx == agents_col["Localiza瀣o"]:
                    agent.location = cell.value
                elif cell.col_idx == agents_col["Site"]:
                    agent.website = cell.value
                elif cell.col_idx == agents_col["Facebook"]:
                    agent.facebook = cell.value
                elif cell.col_idx == agents_col["Twitter"]:
                    agent.twitter = cell.value
                elif cell.col_idx == agents_col["Google+"]:
                    agent.google_plus = cell.value
                elif cell.col_idx == agents_col["Instagram"]:
                    agent.instagram = cell.value
                elif cell.col_idx == agents_col["Nome Fantasia"]:
                    agent.company_name = cell.value
                elif cell.col_idx == agents_col["C󀤀igo da Natureza Jur퀤ica"]:
                    agent.cnpj = cell.value
                elif cell.col_idx == agents_col["Atividade Principal"]:
                    agent.main_activity = cell.value
                elif cell.col_idx == agents_col["Nome ou Raz〯 Social"]:
                    agent.corporate_name = cell.value
                elif cell.col_idx == agents_col["Data de Funda瀣o (Opcional)"]:
                    agent.foundation = cell.value
                elif cell.col_idx == agents_col["CNPJ"]:
                    agent.codigo_natureza_juridica = cell.value
                elif cell.col_idx == agents_col["Mesorregi〯"]:
                    agent.mesoregion = cell.value
                elif cell.col_idx == agents_col["Microrregi〯"]:
                    agent.microregion = cell.value
                elif cell.col_idx == agents_col["Nome da aba oportunidade"]:
                    agent.opportunity_tab_name = cell.value
                elif cell.col_idx == agents_col["Usar a aba oportunidades?"]:
                    if cell.value.__str__().strip == "" or cell.value is None:
                        agent.use_opportunity_tab = False
                    else:
                        agent.use_opportunity_tab = cell.value
            agents.append(agent)
        return agents

    @staticmethod
    def parse_agent_json1(agents):
        _agents = []
        for _agent in agents:
            if _agent is not None:
                agent = Agent()
                agent.agent_identifier = _agent['id']
                agent.name = _agent['name']
                agent.latitude = _agent['location']['latitude']
                agent.longitude = _agent['location']['longitude']
                agent.created_at = _agent['createTimestamp']['date']
                agent.parent_entity = _agent['parent']
                agent.city = _agent['geoMunicipio']
                _agents.append(agent)
                print(agent)
        return _agents