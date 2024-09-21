import feedparser
import os
from datetime import datetime

# URL do feed RSS
feed_url = 'https://docsvaticanosegundo.blogspot.com/feeds/posts/default'
feed = feedparser.parse(feed_url)

# Caminho para salvar o arquivo HTML no seu projeto GitHub Pages
output_html_path = 'postagens.html'

# Início do template HTML
html_content = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Últimas Postagens</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Últimas Postagens do Blog</h1>
    <div id="postagens">
'''

# Loop através das postagens do feed RSS
for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = datetime(*entry.published_parsed[:6]).strftime('%d/%m/%Y')
    summary = entry.summary  # Conteúdo da postagem (ou resumo)

    # Adiciona o conteúdo da postagem ao HTML
    html_content += f'''
    <div class="postagem">
        <h2>{title}</h2>
        <p><em>Publicado em: {published}</em></p>
        <p>{summary}</p>
        <p><a href="{link}" target="_blank">Leia mais</a></p>
    </div>
    <hr>
    '''

# Final do template HTML
html_content += '''
    </div>
</body>
</html>
'''

# Salvar o HTML no arquivo
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f'Arquivo {output_html_path} atualizado com sucesso!')
