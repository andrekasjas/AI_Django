import spacy
from django.shortcuts import render

nlp = spacy.load('es_core_news_md')

def analisis_sentimientos(request):
    if request.method == 'POST':
        # Obtener el texto a analizar
        texto = request.POST['texto']

        # Procesar el texto con SpaCy
        doc = nlp(texto)
        # Obtener el sentimiento del texto
        sentimiento = doc.sentiment
        # Pasar el resultado a la plantilla HTML como contexto
        if sentimiento > 0:
            sentimiento = "Positivo"
        elif sentimiento < 0:
            sentimiento = "Negativo"
        else:
            sentimiento = "Neutro"
        context = {
            'texto': texto,
            'sentimiento': sentimiento,
        }
        # Renderizar la plantilla HTML y devolverla como respuesta
        return render(request, 'analisis_sentimientos.html', context)
    return render(request, 'analisis_sentimientos.html')
