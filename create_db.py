from main import app, db, Projeto

with app.app_context():
    db.create_all()

    projeto1 = Projeto(
        titulo="Bot de Notificação de Preços",
        descricao="Um script que monitora preços de produtos em um e-commerce e envia notificações por Telegram quando o preço cai.",
        imagem="img/placeholder-automacao-1.jpg",
        link_github="https://github.com/seu-usuario/seu-repo-1",
        conteudo="Esse projeto faz isso blablablablaa",
    )
    projeto2 = Projeto(
        titulo="Organizador de Arquivos",
        descricao="Ferramenta que organiza automaticamente arquivos de uma pasta (ex: Downloads) em subpastas baseadas na extensão do arquivo.",
        imagem="img/placeholder-automacao-2.jpg",
        link_github="https://github.com/seu-usuario/seu-repo-2",
        conteudo="Esse projeto faz isso blablablablaa",
    )
    
    # Adicionando projetos de web como exemplo para o futuro
    projeto3 = Projeto(
        titulo="Blog Pessoal com Flask",
        descricao="Um blog simples construído com Flask e Markdown, permitindo a criação e edição de posts.",
        imagem="img/placeholder-web-1.jpg",
        link_github="https://github.com/seu-usuario/seu-repo-3",
        conteudo="Esse projeto faz isso blablablablaa",
        )
    
    db.session.add(projeto1)
    db.session.add(projeto2)
    db.session.add(projeto3)

    db.session.commit()