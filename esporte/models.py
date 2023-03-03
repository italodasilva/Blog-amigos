from django.db import models

FAV_CURSOS = [
    ('INFORMÁTICA', 'Informática'),
    ('TELEMARKTING', 'Telemarkting'),
    ('COSTURA', 'Costura'),
    ('ELÉTRICA', 'Elétrica'),
    ('ADMINISTRATIVO', 'Administrativo'),
    ('SECRETARIADO', 'Secretariado'),
]

FAV_SEXO = [
    ('MASCULINO', 'Masculino'),
    ('FEMININO', 'Feminino'),
]

FAV_ESTADO = [
    ('ACRE', 'AC'),
    ('ALAGOAS', 'AL'),
    ('AMAPÁ', 'AP'),
    ('AMAZONAS', 'AM'),
    ('BAHIA', 'BA'),
    ('CEARÁ', 'CE'),
    ('DISTRITO FEDERAL', 'DF'),
    ('ESPÍRITO SANTO', 'ES'),
    ('GOIÁS', 'GO'),
    ('MARANHÃO', 'MA'),
    ('MATO GROSSO', 'MT'),
    ('MATO GROSSO DO SUL', 'MS'),
    ('MINAS GERAIS', 'MG'),
    ('PARÁ', 'PA'),
    ('PARAÍBA', 'PB'),
    ('PARANÁ', 'PR'),
    ('PERNAMBUCO', 'PE'),
    ('PIAUÍ', 'PI'),
    ('RIO DE JANEIRO', 'RJ'),
    ('RIO GRANDE DO NORTE', 'RN'),
    ('RIO GRANDE DO SUL', 'RS'),
    ('RONDÔNIA', 'RO'),
    ('RORÔIMA', 'RR'),
    ('SANTA CATARINA', 'SC'),
    ('SÃO PAULO', 'SP'),
    ('SERGIPE', 'SE'),
    ('TOCÂNTIS', 'TO'),
]

FAV_PCD = [
    ('SIM', 'Sim'),
    ('NÃO', 'Não'),
]

class Atividade(models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to='beleza/img', blank=True)
    nome = models.CharField(max_length=200, null=True, verbose_name='DIGITE O NOME DO CURSO:', help_text='O nome do curso aparecerá como opção para o aluno.')
    descricao = models.TextField(null=True)
    def __str__(self):
        return self.nome

class Esporte(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False, verbose_name='NOME COMPLETO:')
    CPF = models.CharField(max_length=14, null=True, unique=True, verbose_name='DIGITE O SEU CPF:', help_text='Coloque os . e os - : Ex: 000.000.000-00')
    sexo = models.CharField(max_length=50, choices=FAV_SEXO, null=True, verbose_name='INFORME SEU SEXO:')
    nascimento = models.CharField(max_length=10, null=True, verbose_name='INFORME SUA DATA DE NASCIMENTO:', help_text='Coloque as / : Ex: 00/00/0000')
    email = models.EmailField(null=True, verbose_name='INFORME SEU E-MAIL:')
    celular = models.CharField(max_length=14, null=True, verbose_name='DIGITE O NÚMERO DO SEU CELULAR:', help_text='Coloque o DDD em ( ) : Ex: (31)9999-9999')
    IdAtividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, verbose_name='ESCOLHA O CURSO QUE VOCÊ DESEJA CURSAR', null=True)
    cep = models.CharField(max_length=9, null=True, verbose_name='INFORME SEU CEP')
    estado = models.CharField(max_length=200, choices=FAV_ESTADO, null=True, verbose_name='UF:')
    cidade = models.CharField(max_length=100, null=True, verbose_name='MUNICIPIO')
    bairro = models.CharField(max_length=200, null=True, verbose_name='BAIRRO:')
    rua = models.CharField(max_length=200, null=True, verbose_name='RUA:')
    numero = models.IntegerField(null=True, verbose_name='N°:')
    complemento = models.CharField(max_length=30, null=True, verbose_name='COMPLEMENTO:')
    pcd = models.CharField(max_length=3, choices=FAV_PCD, null=True, verbose_name='INFORME SE VOCÊ É PCD:')

    def __str__(self):
        return self.nome
