import discord
import config

token = config.token

client = discord.Client()

@client.event #wrapper
async def on_ready():
    print(f"Logado como {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "!diarios" == message.content.lower():
        await message.channel.send("""
`!deve - Guia do diários de Deve
!dorin - Guia dos diários de Dorin
!agris - Guia dos diários de Agris (Magahan)
!bartali - Guia dos diários de Bartali`""")

    elif "!deve" == message.content.lower():
        await message.channel.send("http://bit.ly/devediario por `@PandaDruj twitch.tv/pandadruj`")

    elif "!dorin" == message.content.lower():
        await message.channel.send("https://tinyurl.com/dorinmorgrim por `@PandaDruj twitch.tv/pandadruj`")

    elif "!fps" == message.content.lower():
        await message.channel.send("https://tinyurl.com/bdoperformance por `@PandaDruj twitch.tv/pandadruj`")

    elif "!agris" == message.content.lower():
        await message.channel.send("https://tinyurl.com/diarioagris por `@PandaDruj twitch.tv/pandadruj`")

    elif "!bartali" == message.content.lower():
        await message.channel.send("https://docs.google.com/document/d/1JUN7uqO4y18ysy6bR778SLeLs3Kt5zDQ8ndXjkLBBok/edit?usp=sharing`")

    elif "tchau" in message.content.lower():
        await message.channel.send("Até mais! :heart:")

    elif "!buffxp" == message.content.lower():
        await message.channel.send("""
        Experiência de Mercenário – 200% (Recompença Diária no Y) - pode-se juntar 3x através da "Alquimia Simples" para obter scroll 600%
Pergaminho XP ou Livro de Combate – 100%
Comida – Cron Simples – 20%
Elixir da Fera – 20%
Buff do Espírito Negro (lvl 50+) – 20%
Sino – 100%
Buff do Padre – 3% a 15%
Pra pegar esse buff você precisa conversasr com o Padre em cada cidade e levar 5 barras de ouro de 1G. Pra cada tentativa ele pode te dar de 3% a 15% de Buff de XP. Cada tentativa custa 5 barras de ouro de 1G.
2x Cristais "Experiência (elmo)" 20% XP
Cristais "HON Gervish" - 5% combo 4 cristais
Cristais "HON Makalod" - 5% combo 4 cristais

Buffs P2w
Pacote Econômico – 30%
Barraca – Habilidade de Experiência – 10%
Costume de Cash – 10%
Lua Minguante – 100% (Item de Cash)""")

    elif "!cdw" == message.content.lower():
        await message.channel.send("""https://discord.gg/5k6pQem
http://cdw-app-gameguild.herokuapp.com""")

    elif "!invictus" == message.content.lower():
        await message.channel.send("https://www.youtube.com/channel/UCCcMcEEZ0aIkJx7dx39G4BA")

    elif "!tesouros" == message.content.lower():
        await message.channel.send("""`Tente um dos seguintes comandos: 
!mapa 
!bussola 
!pothp 
!potmp`""")

    elif "!mapa" == message.content.lower():
        img = discord.File("img/mapa.jpg", filename="img/mapa.jpg")
        await message.channel.send(file=img)

    elif "!bussola" == message.content.lower():
        img = discord.File("img/bussola.jpg", filename="img/bussola.jpg")
        await message.channel.send(file=img)

    elif "!pothp" == message.content.lower():
        img = discord.File("img/pot_hp.jpg", filename="img/Pot_hp.jpg")
        await message.channel.send(file=img)

    elif "!potmp" == message.content.lower():
        img = discord.File("img/pot_wp.jpg", filename="img/pot_wp.jpg")
        await message.channel.send(file=img)

    elif "!hystria" == message.content.lower():
        img = discord.File("img/hystria.png", filename="img/hystria.png")
        await message.channel.send(file=img)

    elif "!portais" == message.content.lower():
        img = discord.File("img/portais.png", filename="img/portais.png")
        await message.channel.send(file=img)

    elif "!permuta" == message.content.lower():
        await message.channel.send("""
`Tente um dos seguntes comandos:
!rotas - Quantidade de permutas para liberar novas rotas
!barcos - As variações de expansão de Veleiro/Fragata disponíveis
!craftbarcos - Guia de materiais para craft dos barcos
!itensmercante - Itens azuis do navio Mercante para se fazer a Carraca`""")

    elif "!rotas" == message.content.lower():
        img = discord.File("img/rotasimg.png", filename="img/rotasimg.png")
        await message.channel.send(file=img)

    elif "!barcos" == message.content.lower():
        img = discord.File("img/vbarcos.png", filename="img/vbarcos.png")
        await message.channel.send(file=img)

    elif "!craftbarcos" == message.content.lower():
        await message.channel.send("https://docs.google.com/spreadsheets/d/1vp4vOd0IxiQ-GuQbBckrgRW_1AU0e2g-J7eIPWbvRzE/edit#gid=791526731")

    elif "!itensmercante" == message.content.lower():
        img = discord.File("img/imgmercante.png", filename="img/imgmercante.png")
        await message.channel.send(file=img)

    elif "!db" == message.content.lower():
        await message.channel.send("http://bdocodex.com/pt")

    elif "!discord" == message.content.lower():
        await message.channel.send("https://discord.gg/uktPzFH")

    elif "!discordclasses" == message.content.lower():
        await message.channel.send("""
Tente um dos seguinte comandos:

`!musa - Discord das classes Musah/Maehwa
!maehwa - Discord das Maehwa/Musa
!ninja - Discord das classes Ninja/Kuno
!ranger - Discord da classe Caçadora
!sorc - Discord da classe Feiticeira
!tamer - Discord da classe Domadora
!valk - Discord da classe Valquíria
!warrior - Discord da classe Guerreiro
!witch - Discord das classes Bruxa/Mago
!wiz - Discord das classes Mago/Bruxa
!zerk - Discord da classe Berserker
!dk - Discord da classe Cavaleira das Trevas
!striker - Discord da classe Lutador/Mística
!mystic - Discord da classe Mística/Lutador
!lahn - Discord da classe Lahn
!archer - Discord da classe Arqueiro
!shai - Discord da classe Shai
!guardian - Discord da classe Guardiã`
""")

    elif "!musa" == message.content.lower():
        await message.channel.send("https://discord.gg/6ThcWqx")
    elif "!maehwa" == message.content.lower():
        await message.channel.send("https://discord.gg/6ThcWqx")
    elif "!ninja" == message.content.lower():
        await message.channel.send("https://discord.gg/VSuuF5g")
    elif "!kuno" == message.content.lower():
        await message.channel.send("https://discord.gg/VSuuF5g")
    elif "!ranger" == message.content.lower():
        await message.channel.send("https://discord.gg/J2Andmk")
    elif "!sorc" == message.content.lower():
        await message.channel.send("https://discord.gg/GWz9SNd")
    elif "!tamer" == message.content.lower():
        await message.channel.send("https://discord.gg/zn6puC6")
    elif "!valk" == message.content.lower():
        await message.channel.send("https://discord.gg/XrzrZzn")
    elif "!warrior" == message.content.lower():
        await message.channel.send("https://discord.gg/6s3ZBRN")
    elif "!witch" == message.content.lower():
        await message.channel.send("https://discord.gg/tsSvKsG")
    elif "!wiz" == message.content.lower():
        await message.channel.send("https://discord.gg/tsSvKsG")
    elif "!zerk" == message.content.lower():
        await message.channel.send("https://discord.gg/83Ny223")
    elif "!dk" == message.content.lower():
        await message.channel.send("http://discord.gg/nF6xb3g https://discord.gg/G6KfErT")
    elif "!striker" == message.content.lower():
        await message.channel.send("https://discord.gg/fRWVwRD")
    elif "!mystic" == message.content.lower():
        await message.channel.send("https://discord.gg/fRWVwRD")
    elif "!lahn" == message.content.lower():
        await message.channel.send("https://discord.gg/nRBXMtW")
    elif "!archer" == message.content.lower():
        await message.channel.send("https://discord.gg/NfvbMZe")
    elif "!shai" == message.content.lower():
        await message.channel.send("https://discord.gg/vq68zAG")
    elif "!guardian" == message.content.lower():
        await message.channel.send("https://discord.gg/9jdEmYp")

    elif "!comandos" == message.content.lower():
        await message.channel.send("""
`Comandos disponíveis:
!diarios - Guia dos diários
!buffxp - Buffs para Leveling
!cdw - Discord e site da CDW
!fps - Guia para melhorar a performance do BDO
!tesouros - Itens tesouro do BDO
!portais - Possíveis locais dos portais Aakman/Hystria no deserto
!hystria - Mapa das rotações de Hystria
!permuta - Informações referentes a permuta
!db - Database dos itens do BDO
!discordclasses - Discord das classes do jogo`""")

client.run(token)

