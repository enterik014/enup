import questions as questions
import layout

question = questions.Question()

question.year = 2021
question.number = 117

question.add_context('title', text='TEXTO 1')
question.add_context('text', text='Com o aumento da população de suínos no Brasil, torna-se necessária a adoção de métodos para reduzir o potencial poluidor dos resíduos dessa agroindústria, uma vez que, comparativamente ao esgoto doméstico, os dejetos suínos são 200 vezes mais poluentes. Sendo assim, a utilização desses resíduos como matéria-prima na obtenção de combustíveis é uma alternativa que permite diversificar a matriz energética nacional, ao mesmo tempo em que parte dos recursos hídricos do país são preservados.')
question.add_context('source', text='BECK, A. M. Resíduos suínos como alternativa energética sustentável. XXVII Encontro Nacional de Engenharia de Produção. Anais ENEGEP, Foz do Iguaçu, 2007 (adaptado).')
question.statement = 'O biocombustível a que se refere o texto é o'

question.add_context('image', path='images/image.jpeg')

question.add_alternative('etanollllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll')
question.add_alternative(path='images/image.jpeg')
question.add_alternative(path='images/image.jpeg')
question.add_alternative(path='images/image.jpeg')
question.add_alternative('biodisel')

popup = layout.ENEMpopup()
popup.show(question)