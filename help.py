from pyfiglet import figlet_format
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print
from rich.columns import Columns
import os

console = Console()
TITLE = figlet_format("DARK ARMY HELP", font="small")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def nmap_help():
    table = Table(title="NMAP - Scanner de Rede", show_header=True, header_style="bold yellow")
    table.add_column("Opcao", style="cyan", width=20)
    table.add_column("Descricao", style="white")
    table.add_column("Exemplo", style="green")
    
    table.add_row("-sS", "TCP SYN Scan (stealth)", "nmap -sS 192.168.1.1")
    table.add_row("-sU", "UDP Scan", "nmap -sU 192.168.1.1")
    table.add_row("-sV", "Detecta versoes de servicos", "nmap -sV 192.168.1.1")
    table.add_row("-O", "Detecta sistema operacional", "nmap -O 192.168.1.1")
    table.add_row("-p", "Especifica portas", "nmap -p 80,443,22 192.168.1.1")
    table.add_row("-A", "Scan agressivo (OS + versoes)", "nmap -A 192.168.1.1")
    table.add_row("-sn", "Ping scan apenas", "nmap -sn 192.168.1.0/24")
    table.add_row("-script", "Executa scripts NSE", "nmap --script vuln 192.168.1.1")
    table.add_row("-v", "Modo verbose", "nmap -v 192.168.1.1")
    table.add_row("-Pn", "Ignora discovery", "nmap -Pn 192.168.1.1")
    
    console.print(table)
    
    print("\n[bold white]EXEMPLOS PRATICOS:[/bold white]")
    examples = [
        "[cyan]Scan basico:[/cyan] nmap 192.168.1.1",
        "[cyan]Scan completo:[/cyan] nmap -A -p- 192.168.1.1",
        "[cyan]Scan de rede:[/cyan] nmap -sn 192.168.1.0/24",
        "[cyan]Scan com scripts:[/cyan] nmap --script safe 192.168.1.1"
    ]
    for example in examples:
        print(f"  {example}")
    
    input("\nPressione ENTER para continuar...")

def dird_help():
    table = Table(title="DIRB - Discovery de Diretorios", show_header=True, header_style="bold yellow")
    table.add_column("Opcao", style="cyan", width=20)
    table.add_column("Descricao", style="white")
    table.add_column("Exemplo", style="green")
    
    table.add_row("<url>", "URL alvo", "dirb http://exemplo.com")
    table.add_row("-o", "Salva output em arquivo", "dirb http://exemplo.com -o resultado.txt")
    table.add_row("-a", "Customiza User-Agent", "dirb http://exemplo.com -a 'Mozilla/5.0'")
    table.add_row("-c", "Customiza Cookie", "dirb http://exemplo.com -c 'session=123'")
    table.add_row("-r", "Nao busca recursivamente", "dirb http://exemplo.com -r")
    table.add_row("-X", "Procura por extensoes", "dirb http://exemplo.com -X .php,.txt")
    table.add_row("-N", "Ignora codigos HTTP", "dirb http://exemplo.com -N 404")
    table.add_row("-S", "Modo silencioso", "dirb http://exemplo.com -S")
    table.add_row("-z", "Delay entre requisicoes", "dirb http://exemplo.com -z 100")
    
    console.print(table)
    
    print("\n[bold white]INSTALACAO E USO BASICO:[/bold white]")
    print("[cyan]Instalacao no Linux:[/cyan]")
    print("  sudo apt install dirb")
    print("\n[cyan]Uso basico:[/cyan]")
    print("  dirb http://exemplo.com")
    print("  dirb http://exemplo.com /usr/share/dirb/wordlists/common.txt")
    
    input("\nPressione ENTER para continuar...")

def sqlmap_help():
    table = Table(title="SQLMAP - SQL Injection Automation", show_header=True, header_style="bold yellow")
    table.add_column("Opcao", style="cyan", width=25)
    table.add_column("Descricao", style="white")
    
    table.add_row("-u <url>", "URL alvo para teste")
    table.add_row("--data=<data>", "Dados POST para enviar")
    table.add_row("--cookie=<cookie>", "Cookie de sessao")
    table.add_row("--dbs", "Lista todos databases")
    table.add_row("--current-db", "Mostra database atual")
    table.add_row("--current-user", "Mostra usuario atual")
    table.add_row("--tables", "Lista tabelas do database")
    table.add_row("--columns", "Lista colunas da tabela")
    table.add_row("--dump", "Extrai dados da tabela")
    table.add_row("--dump-all", "Extrai todos os dados")
    table.add_row("--passwords", "Extrai hashes de senhas")
    table.add_row("--os-shell", "Tenta obter shell do OS")
    table.add_row("--level", "Nivel de teste (1-5)")
    table.add_row("--risk", "Risco do teste (1-3)")
    table.add_row("--batch", "Modo automatico")
    table.add_row("--threads", "Numero de threads")
    
    console.print(table)
    
    print("\n[bold white]INSTALACAO:[/bold white]")
    print("git clone https://github.com/sqlmapproject/sqlmap.git")
    print("cd sqlmap")
    print("python sqlmap.py --version")
    
    print("\n[bold white]EXEMPLOS PRATICOS:[/bold white]")
    examples = [
        "[cyan]Teste basico:[/cyan] python sqlmap.py -u 'http://site.com/page.php?id=1'",
        "[cyan]Com dados POST:[/cyan] python sqlmap.py -u 'http://site.com/login' --data='user=admin&pass=123'",
        "[cyan]Com cookie:[/cyan] python sqlmap.py -u 'http://site.com/page.php?id=1' --cookie='session=abc123'",
        "[cyan]Teste completo:[/cyan] python sqlmap.py -u 'http://site.com/page.php?id=1' --dbs --tables --batch"
    ]
    for example in examples:
        print(f"  {example}")
    
    input("\nPressione ENTER para continuar...")

def sherma_dos_help():
    print(Panel.fit("SHERMA DDOS TOOL", style="bold yellow"))
    
    print("[bold white]DESCRICAO:[/bold white]")
    print("Ferramenta para testes de estresse e DDoS desenvolvida por vøidh7")
    
    print("\n[bold white]INSTALACAO:[/bold white]")
    steps = [
        "git clone https://github.com/voidh7/sherma-ddos-tool",
        "cd sherma-dos-tool",
        "pip install -e ."
    ]
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")
    
    print("\n[bold white]OPCOES:[/bold white]")
    options = [
        ("-v", "Modo verbose"),
        ("-t", "Define numero de threads"),
        ("-p", "Define numero de requests"),
        ("-T", "Timeout das requisicoes")
    ]
    for opt, desc in options:
        print(f"  [cyan]{opt}[/cyan] - {desc}")
    
    print("\n[bold white]EXEMPLOS:[/bold white]")
    print("  python3 sherma.py http://exemplo.com -v -t 10")
    print("  python3 sherma.py http://exemplo.com -t 50 -p 1000")
    
    input("\nPressione ENTER para continuar...")

def tool_util():
    tools_info = {
        "WGET": {
            "desc": "Baixa arquivos da web",
            "inst": "Ja incluso na maioria das distros Linux",
            "exemplos": [
                "wget http://exemplo.com/arquivo.txt",
                "wget -O saida.txt http://exemplo.com/arquivo",
                "wget --limit-rate=100k http://exemplo.com/largefile.iso"
            ]
        },
        "CURL": {
            "desc": "Faz requisicoes HTTP e transfere dados",
            "inst": "Ja incluso na maioria das distros Linux",
            "exemplos": [
                "curl -v http://exemplo.com",
                "curl -X POST http://exemplo.com/api -d 'dados=valor'",
                "curl -H 'Authorization: Bearer token' http://api.com"
            ]
        },
        "NGROK": {
            "desc": "Tunelamento para expor servicos locais",
            "inst": "Baixar de https://ngrok.com/download",
            "exemplos": [
                "ngrok http 3000",
                "ngrok tcp 8080",
                "ngrok udp 3030",
                "ngrok http 80 --hostname meu-subdominio.ngrok.io"
            ]
        },
        "UTILITARIOS DE REDE": {
            "desc": "Ferramentas basicas de diagnostico",
            "inst": "Geralmente pre-instaladas",
            "exemplos": [
                "which python3          # Localiza binario",
                "whois exemplo.com      # Informacoes de dominio",
                "nslookup exemplo.com   # Resolucao DNS",
                "host exemplo.com       # Resolucao DNS alternativa"
            ]
        },
        "APIS UTEIS": {
            "desc": "APIs para consulta de informacoes",
            "inst": "Usar com curl ou wget",
            "exemplos": [
                "curl https://apiutilities.vercel.app/meu-ip",
                "curl https://ipinfo.io/8.8.8.8/json",
                "curl https://httpbin.org/ip"
            ]
        }
    }
    
    for tool, info in tools_info.items():
        print(Panel.fit(
            f"[bold white]{tool}[/bold white]\n\n"
            f"[cyan]Descricao:[/cyan] {info['desc']}\n"
            f"[cyan]Instalacao:[/cyan] {info['inst']}\n"
            f"[cyan]Exemplos:[/cyan]\n" + 
            "\n".join([f"  {ex}" for ex in info['exemplos']]),
            style="bold yellow"
        ))
    
    input("\nPressione ENTER para continuar...")

def tools_menu():
    while True:
        clear_screen()
        print(f"[red]{TITLE}[/red]")
        print("by vøidh7")
        print(Panel.fit("FERRAMENTAS E EXPLOITS", style="bold cyan"))
        
        menu_options = [
            "[1] NMAP Help - Scanner de rede",
            "[2] DIRB Help - Discovery de diretorios", 
            "[3] SQLMAP Help - SQL Injection",
            "[4] SHERMA DOS Help - Teste de estresse",
            "[5] Utilitarios do Sistema",
            "[0] Voltar ao Menu Principal"
        ]
        
        for option in menu_options:
            print(option)
        
        try:
            choice = int(input("\n > "))
        except ValueError:
            print("[red]Entrada invalida. Digite um numero.[/red]")
            input("Pressione ENTER para continuar...")
            continue

        if choice == 0:
            return
        elif choice == 1:
            nmap_help()
        elif choice == 2:
            dird_help()
        elif choice == 3:
            sqlmap_help()
        elif choice == 4:
            sherma_dos_help()
        elif choice == 5:
            tool_util()
        else:
            print("[red]Opcao invalida.[/red]")
            input("Pressione ENTER para continuar...")

def bots_menu():
    while True:
        clear_screen()
        print(f"[red]{TITLE}[/red]")
        print("by vøidh7")
        print(Panel.fit("BOTS E AUTOMACOES", style="bold cyan"))
        
        print("[1] WhatsApp Bots")
        print("[2] Web Bots")
        print("[0] Voltar")
        
        try:
            choice = int(input(" > "))
        except ValueError:
            print("[red]Entrada invalida.[/red]")
            continue

        if choice == 0:
            return
        elif choice == 1:
            print(Panel.fit(
                "GREGORY BOT v0.5\n\n"
                "[cyan]Descricao:[/cyan] Bot de diversao para grupos do WhatsApp\n"
                "[cyan]Base:[/cyan] Takishi Bot\n"
                "[cyan]Desenvolvedores:[/cyan] vøidh7 and justin\n"
                "[cyan]Caracteristicas:[/cyan] 100% editavel\n"
                "[cyan]Link:[/cyan] https://github.com/voidh7/Gregory-BotV1/",
                style="bold green"
            ))
        elif choice == 2:
            print(Panel.fit(
                "BOBY-AGENT\n\n"
                "[cyan]Descricao:[/cyan] Agente de IA capaz de baixar videos e responder perguntas\n"
                "[cyan]Desenvolvedor:[/cyan] adm caio multiverso\n"
                "[cyan]Link:[/cyan] https://boby-agent.vercel.app",
                style="bold green"
            ))
        
        input("\nPressione ENTER para continuar...")

def redes_sociais():
    print(Panel.fit("REDES SOCIAIS DA DARK ARMY", style="bold cyan"))
    
    redes = {
        "SITE OFICIAL": "(em breve)",
        "WHATSAPP CHANNEL (PRINCIPAL)": "https://whatsapp.com/channel/0029Vb6HSTAId7nLGLxemc0v",
        "BRASIL.DEV CHANNEL": "https://whatsapp.com/channel/0029Vb8DlDL9MF95R8e8Px1o", 
        "BRASIL.DEV TELEGRAM": "https://t.me/brasildevofc/",
        "vøidh7 GITHUB": "https://github.com/voidh7",
        "darkZer0 GITHUB": "https://github.com/DarkZer010/"
    }
    
    for rede, link in redes.items():
        print(f"[bold white]{rede}:[/bold white]")
        print(f"  [cyan]{link}[/cyan]\n")
    
    input("Pressione ENTER para continuar...")

def inicial_menu():
    while True:
        clear_screen()
        print(f"[red]{TITLE}[/red]")
        print("by vøidh7\n")
        print(Panel.fit("MENU PRINCIPAL - DARK ARMY HELP", style="bold red"))
        
        menu_options = [
            "[1] Ferramentas de Seguranca",
            "[2] Protocolos de Rede", 
            "[3] Inteligencia Artificial",
            "[4] Bots e Automacoes",
            "[5] Redes Sociais",
            "[0] Sair do Programa"
        ]
        
        for option in menu_options:
            print(option)

        try:
            escolha = int(input("\n > "))
        except ValueError:
            print("[red]Entrada invalida. Digite um numero.[/red]")
            input("Pressione ENTER para continuar...")
            continue

        if escolha == 0:
            print("[green]Saindo do Dark Army Help...[/green]")
            break
        elif escolha == 1:
            tools_menu()
        elif escolha == 2:
            print(Panel.fit(
                "PROTOCOLOS DE REDE\n\n"
                "Em desenvolvimento...\n"
                "Esta secao contera informacoes sobre:\n"
                "- TCP/IP\n- UDP\n- HTTP/HTTPS\n- DNS\n- SSH\n- FTP",
                style="bold yellow"
            ))
            input("Pressione ENTER para continuar...")
        elif escolha == 3:
            print(Panel.fit(
                "INTELIGENCIA ARTIFICIAL\n\n"
                "Em desenvolvimento...\n"
                "Esta secao contera informacoes sobre:\n"
                "- Machine Learning para seguranca\n"
                "- Automacao com IA\n"
                "- Ferramentas de IA para pentesting",
                style="bold yellow"
            ))
            input("Pressione ENTER para continuar...")
        elif escolha == 4:
            bots_menu()
        elif escolha == 5:
            redes_sociais()
        else:
            print("[red]Opcao invalida.[/red]")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    inicial_menu()
