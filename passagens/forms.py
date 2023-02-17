from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.models import Passagem, ClasseViagem, Pessoa

from passagens.validation import *

class PassagemForms(forms.ModelForm):
    
    data_pesquisa = forms.DateField(label='Data pesquisa', disabled=True, initial=datetime.today)
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': "Data de ida",
            'data_volta':"Data da volta",
            'informacoes':'Informações',
            'classe_viagem':'Classe do vôo',
            }

        widgets = {
            'data_ida':DatePicker(),
            'data_volta':DatePicker(),
        }
        
    
    
    def clean(self):
        """Esse metodo aplica validações 
        \n * Se Destino e Origem são Iguais, 
        \n * Verifica digitos númericos no campos origem e destino
        \n * Verifica as datas de viagem
        \n * Se existe erros atribuir erros ao campo para correção 
         """
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        list_errors = {}

        if identicos(origem, destino):
            list_errors['destino'] = 'Origem e destino precisam ser diferentes'
        if check_caracter(origem):
            list_errors['origem'] = 'O Campo origem não permite digitos númericos'
        if check_caracter(destino):
            list_errors['destino'] = 'O Campo destino não permite digitos númericos'
        if maior(data_ida, data_volta):
            list_errors['data_volta'] = 'A data do retorno precisa ser maior que a de ida '
        if maior(data_pesquisa, data_ida):
            list_errors['data_ida'] = 'Data invalida, verificar a data!'

        if list_errors != None:
            for error in list_errors:
                messeger_error = list_errors[error]
                self.add_error(error, messeger_error)
            return self.cleaned_data

class Pessoaforms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['email']





# CLASSE_CHOICE = {
#     (1, 'Economica'),
#     (2, 'Executiva'),
#     (3, 'Primeira Classe')

# }
# class PassagemForms(forms.Form):
#     origem = forms.CharField(label='Origem', max_length=100)
#     destino = forms.CharField(label='Destino', max_length=100)
#     data_ida = forms.DateField(label='Ida', widget=DatePicker())
#     data_volta = forms.DateField(label='Volta', widget=DatePicker())
#     data_pesquisa = forms.DateField(label='Data pesquisa', disabled=True, initial=datetime.today)
#     classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=CLASSE_CHOICE)
#     informacoes = forms.CharField(
#         label='Informações extra',
#         max_length=200,
#         widget=forms.Textarea(),
#         required=False)
#     email = forms.EmailField(label="E-mail",max_length=120)


    
#     def clean(self):
#         """Esse metodo aplica validações 
#         \n * Se Destino e Origem são Iguais, 
#         \n * Verifica digitos númericos no campos origem e destino
#         \n * Verifica as datas de viagem
#         \n * Se existe erros atribuir erros ao campo para correção 
#          """
#         origem = self.cleaned_data.get('origem')
#         destino = self.cleaned_data.get('destino')
#         data_ida = self.cleaned_data.get('data_ida')
#         data_volta = self.cleaned_data.get('data_volta')
#         data_pesquisa = self.cleaned_data.get('data_pesquisa')
#         list_errors = {}

#         if identicos(origem, destino):
#             list_errors['destino'] = 'Origem e destino precisam ser diferentes'
#         if check_caracter(origem):
#             list_errors['origem'] = 'O Campo origem não permite digitos númericos'
#         if check_caracter(destino):
#             list_errors['destino'] = 'O Campo destino não permite digitos númericos'
#         if maior(data_ida, data_volta):
#             list_errors['data_volta'] = 'A data do retorno precisa ser maior que a de ida '
#         if maior(data_pesquisa, data_ida):
#             list_errors['data_ida'] = 'Data invalida, verificar a data!'

#         if list_errors != None:
#             for error in list_errors:
#                 messeger_error = list_errors[error]
#                 self.add_error(error, messeger_error)
#             return self.cleaned_data

