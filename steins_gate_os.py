#!/usr/bin/env python3
"""
Steins;GateOS - Future Gadget Laboratory Operating System
Testing Phase α

A terminal-based OS simulation inspired by the Steins;Gate universe.
"""

import os
import sys
import time
import datetime
import random
from typing import Dict, List, Any

class SteinsGateOS:
    def __init__(self):
        self.current_user = "okabe"
        self.world_line = 1.130205
        self.running = True
        self.lab_members = {
            "001": {"name": "Okabe Rintaro", "title": "Mad Scientist", "status": "Online"},
            "002": {"name": "Makise Kurisu", "title": "Assistant", "status": "Online"}, 
            "003": {"name": "Mayuri Shiina", "title": "Hostage", "status": "Online"},
            "004": {"name": "Itaru Hashida", "title": "Super Hacker", "status": "Online"},
            "005": {"name": "Suzuha Amane", "title": "Part-time Warrior", "status": "Offline"},
            "006": {"name": "Moeka Kiryu", "title": "Shining Finger", "status": "Unknown"},
            "007": {"name": "Ruka Urushibara", "title": "Lukako", "status": "Online"},
            "008": {"name": "Faris NyanNyan", "title": "NyanNyan", "status": "Online"}
        }
        
        self.future_gadgets = {
            "001": {"name": "Bit Particle Cannon", "status": "Prototype", "function": "Particle Physics"},
            "002": {"name": "Bamboo-copter Camera", "status": "Active", "function": "Surveillance"},
            "003": {"name": "Televised Ouija Board", "status": "Inactive", "function": "Communication"},
            "004": {"name": "Moad Snake", "status": "Prototype", "function": "Intelligence Gathering"},
            "005": {"name": "Upa", "status": "Active", "function": "Mascot/Luck Charm"},
            "006": {"name": "36th Cyborg", "status": "Broken", "function": "Combat Support"},
            "007": {"name": "CRT Editor", "status": "Active", "function": "Video Editing"},
            "008": {"name": "Phone Microwave", "status": "CLASSIFIED", "function": "Time Travel Device"}
        }
        
        self.dmail_history = []
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_banner(self):
        """Display the OS banner"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                        STEINS;GATE OS - α Testing Phase                      ║
║                      Future Gadget Laboratory System                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║    ███████╗████████╗███████╗██╗███╗   ██╗███████╗     ██████╗  ██████╗       ║
║    ██╔════╝╚══██╔══╝██╔════╝██║████╗  ██║██╔════╝    ██╔═══██╗██╔════╝       ║
║    ███████╗   ██║   █████╗  ██║██╔██╗ ██║███████╗    ██║   ██║███████╗       ║
║    ╚════██║   ██║   ██╔══╝  ██║██║╚██╗██║╚════██║    ██║   ██║╚════██║       ║
║    ███████║   ██║   ███████╗██║██║ ╚████║███████║    ╚██████╔╝███████║       ║
║    ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝     ╚═════╝ ╚══════╝       ║
║                                                                              ║
║                        "The choice of Steins Gate"                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

World Line Divergence: {:.6f}%
Lab Status: OPERATIONAL
Security Level: α-Class
Time Leap Machine: STANDBY

Type 'help' for available commands.
""".format(self.world_line)
        print(banner)
        
    def get_prompt(self):
        """Get the command prompt"""
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"[Lab-{current_time}]@{self.current_user}:~$ "
        
    def cmd_help(self, args):
        """Display help information"""
        help_text = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                              AVAILABLE COMMANDS                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║ help        - Display this help message                                      ║
║ time        - Show current time and world line status                        ║
║ lab         - Display lab member information                                 ║
║ gadgets     - List future gadgets and their status                          ║
║ dmail       - Access the D-Mail system                                      ║
║ divergence  - Check current world line divergence                           ║
║ clear       - Clear the terminal screen                                     ║
║ status      - Show detailed system status                                   ║
║ quote       - Display a random Steins;Gate quote                           ║
║ exit        - Exit the OS                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
        print(help_text)
        
    def cmd_time(self, args):
        """Display time and world line information"""
        current_time = datetime.datetime.now()
        print(f"\n╔══════════════════════════════════════════════════════════════╗")
        print(f"║                        TIME OPERATIONS                       ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║ Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}                     ║")
        print(f"║ World Line:   {self.world_line:.6f}%                         ║")
        print(f"║ Timeline:     α Attractor Field                              ║")
        print(f"║ Status:       CONVERGENT                                     ║")
        print(f"╚══════════════════════════════════════════════════════════════╝\n")
        
    def cmd_lab(self, args):
        """Display lab member information"""
        print(f"\n╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                           LAB MEMBER DATABASE                                ║")
        print(f"╠══════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ ID  │ NAME              │ TITLE               │ STATUS                    ║")
        print(f"╠═════╪═══════════════════╪═════════════════════╪═══════════════════════════╣")
        
        for member_id, info in self.lab_members.items():
            status_color = "🟢" if info["status"] == "Online" else "🔴" if info["status"] == "Offline" else "🟡"
            print(f"║ {member_id} │ {info['name']:<17} │ {info['title']:<19} │ {status_color} {info['status']:<21} ║")
            
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝\n")
        
    def cmd_gadgets(self, args):
        """Display future gadgets information"""
        print(f"\n╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                          FUTURE GADGET DATABASE                             ║")
        print(f"╠══════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ ID  │ NAME                    │ STATUS       │ FUNCTION                   ║")
        print(f"╠═════╪═════════════════════════╪══════════════╪════════════════════════════╣")
        
        for gadget_id, info in self.future_gadgets.items():
            status_symbol = {
                "Active": "🟢",
                "Prototype": "🟡", 
                "Inactive": "🔴",
                "Broken": "💥",
                "CLASSIFIED": "🔒"
            }.get(info["status"], "❓")
            
            print(f"║ {gadget_id} │ {info['name']:<23} │ {status_symbol} {info['status']:<9} │ {info['function']:<26} ║")
            
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝\n")
        
    def cmd_dmail(self, args):
        """Access D-Mail system"""
        print(f"\n╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                               D-MAIL SYSTEM                                  ║")
        print(f"╠══════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ WARNING: D-Mail transmission may cause timeline divergence!                  ║")
        print(f"║ Current D-Mail capacity: 36 bytes maximum                                   ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝")
        
        if len(args) == 0:
            print("\nD-Mail History:")
            if not self.dmail_history:
                print("  No D-Mails sent yet.")
            else:
                for i, dmail in enumerate(self.dmail_history, 1):
                    print(f"  {i}. {dmail}")
            print("\nUsage: dmail <message> (max 36 characters)")
        else:
            message = " ".join(args)
            if len(message) > 36:
                print(f"ERROR: Message too long! ({len(message)}/36 bytes)")
                print("D-Mail transmission failed. Timeline unchanged.")
            else:
                self.dmail_history.append(message)
                # Slightly shift world line
                self.world_line += random.uniform(-0.000001, 0.000001)
                print(f"D-Mail sent successfully!")
                print(f"Message: {message}")
                print(f"Timeline divergence detected: {self.world_line:.6f}%")
        
    def cmd_divergence(self, args):
        """Check world line divergence"""
        # Add some random fluctuation
        fluctuation = random.uniform(-0.000005, 0.000005)
        current_divergence = self.world_line + fluctuation
        
        print(f"\n╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                          WORLD LINE ANALYSIS                                ║")
        print(f"╠══════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ Current Divergence: {current_divergence:.6f}%                               ║")
        print(f"║ Base Line:          1.130205%                                              ║")
        print(f"║ Attractor Field:    α (Alpha)                                              ║")
        print(f"║                                                                            ║")
        if abs(current_divergence - 1.130205) > 0.000010:
            print(f"║ ⚠️  WARNING: Significant timeline deviation detected!                     ║")
        else:
            print(f"║ ✅ Timeline stable within normal parameters                               ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝\n")
        
    def cmd_clear(self, args):
        """Clear the screen"""
        self.clear_screen()
        self.display_banner()
        
    def cmd_status(self, args):
        """Display system status"""
        uptime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\n╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                            SYSTEM STATUS                                    ║")
        print(f"╠══════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ Lab Computer Status:    OPERATIONAL                                         ║")
        print(f"║ Phone Microwave:        STANDBY                                             ║")
        print(f"║ Time Leap Machine:      INACTIVE                                            ║")
        print(f"║ IBN 5100:              NOT CONNECTED                                        ║")
        print(f"║ SERN Connection:        SECURE                                              ║")
        print(f"║ World Line Monitor:     ACTIVE                                              ║")
        print(f"║ Current User:           {self.current_user.upper()}                                              ║")
        print(f"║ Session Uptime:         {uptime}                                             ║")
        print(f"║ Lab Members Online:     {sum(1 for m in self.lab_members.values() if m['status'] == 'Online')}/8                                                  ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝\n")
        
    def cmd_quote(self, args):
        """Display a random Steins;Gate quote"""
        quotes = [
            "I am mad scientist! It's so cool! Sunovabitch!",
            "The universe has a beginning, but no end. — Infinite.",
            "There is no such thing as chance in this world.",
            "People's feelings are memories that transcend time.",
            "Time is passing so quickly. Right now, I feel like complaining to Einstein.",
            "I'll make you a promise. No matter what world line we're on, I'll find you.",
            "The choice of Steins Gate.",
            "Tutturu~ Mayushii desu!",
            "I am not alone... We are not alone!",
            "Christina! Don't ignore me!"
        ]
        
        quote = random.choice(quotes)
        print(f"\n╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                              RANDOM QUOTE                                   ║")
        print(f"╠══════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ \"{quote}\"")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝\n")
        
    def cmd_exit(self, args):
        """Exit the OS"""
        print("\nShutting down Steins;GateOS...")
        print("Saving world line data...")
        print("Thank you for using Future Gadget Laboratory OS!")
        print("\nEl Psy Kongroo.")
        self.running = False
        
    def parse_command(self, command_line):
        """Parse command line input"""
        parts = command_line.strip().split()
        if not parts:
            return None, []
        return parts[0].lower(), parts[1:]
        
    def execute_command(self, command, args):
        """Execute a command"""
        commands = {
            'help': self.cmd_help,
            'time': self.cmd_time,
            'lab': self.cmd_lab,
            'gadgets': self.cmd_gadgets,
            'dmail': self.cmd_dmail,
            'divergence': self.cmd_divergence,
            'clear': self.cmd_clear,
            'status': self.cmd_status,
            'quote': self.cmd_quote,
            'exit': self.cmd_exit
        }
        
        if command in commands:
            commands[command](args)
        else:
            print(f"Command '{command}' not found. Type 'help' for available commands.")
            
    def run(self):
        """Main OS loop"""
        self.clear_screen()
        self.display_banner()
        
        while self.running:
            try:
                user_input = input(self.get_prompt())
                command, args = self.parse_command(user_input)
                
                if command:
                    self.execute_command(command, args)
                    
            except KeyboardInterrupt:
                print("\n\nForce shutdown detected!")
                print("El Psy Kongroo.")
                break
            except EOFError:
                print("\n\nSession terminated.")
                break

def main():
    """Entry point"""
    try:
        os_instance = SteinsGateOS()
        os_instance.run()
    except Exception as e:
        print(f"Critical system error: {e}")
        print("Timeline corruption detected. Restarting...")
        
if __name__ == "__main__":
    main()