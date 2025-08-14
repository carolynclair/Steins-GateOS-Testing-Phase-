# 🕰️ Steins;Gate OS – *Tuturuu~ First Edition*<imgsrc="Tuturuu%20First%20Edition.png" alt="Steins;Gate OS Preview" width="600">>

> **El Psy Kongroo.**

_A Linux distribution for those who dare to hack the divergence meter of reality._

---

## ✨ Vision Statement

**Steins;Gate OS** is a Debian-based distro that fuses cinematic anime aesthetics with frictionless onboarding and seamless integration.  
It’s designed to be beautiful enough to admire and practical enough for everyday hacking, creating, and time-traveling.

---

## 🎯 Features
- 🎨 Custom wallpapers, icons, and boot animations
- 🖥️ Pre-configured desktop layout for instant immersion
- ⚡ Optimized performance on both old and modern hardware
- 🔧 Easy customization for your own personal timeline

---

## 📦 Installation
```bash
git clone https://github.com/yourusername/Steins-Gate-OS.git
cd Steins-Gate-OS
chmod +x install.sh
./install.sh

---

## ✨ Vision Statement

**Steins;Gate OS** is a Debian-based distro that fuses cinematic anime aesthetics, frictionless onboarding, and native AI integration.  
Designed to be beautiful enough to keep open just to look at, and practical enough for daily work, automation, and AI-assisted tasks.

---

## 🚀 Features

- 🎨 **Cinematic Anime Theming:**  
  Custom Plymouth boot splash, LightDM login, and a Steins;Gate-inspired dark GTK theme.

- 🤖 **MayushiAI:**  
  Your always-cheerful, terminal-based AI companion—“Tuturuu~!”—ready to help, chat, and brighten your day.

- 🖼️ **Wallpapers & Sounds:**  
  Hand-picked Steins;Gate backgrounds and system sounds for a fully immersive experience.

- 🛠️ **Frictionless Onboarding:**  
  First-boot wizard for theme, SFX, and AI setup.

- 🧰 **Pre-installed Essentials:**  
  Firefox ESR, LibreOffice, VS Code OSS, Variety, Conky, and more.

---

## 🛠️ Installation

1. **Download the ISO** (or [build it yourself](#building-the-iso)).
2. **Write to USB** with [Ventoy](https://www.ventoy.net/) or [balenaEtcher](https://www.balena.io/etcher/).
3. **Boot & Install** on your hardware or VM.
4. **Enjoy the divergence!**

---

## 💻 Building the ISO

Clone the repo and build with live-build:

```bash
sudo apt update
sudo apt install live-build
git clone https://github.com/carolynclair/Steins-GateOS-Testing-Phase-.git
cd Steins-GateOS-Testing-Phase-/Steins-Gate_OS/iso/live-build
sudo lb config --distribution bookworm \
  --archive-areas "main contrib non-free non-free-firmware" \
  --mirror-bootstrap http://deb.debian.org/debian/ \
  --mirror-chroot-security http://security.debian.org/debian-security/ \
  --initramfs live-boot
sudo lb build
```

---

## 🤖 MayushiAI Terminal Helper

Launch MayushiAI in any terminal with:

```bash
mayushi
```

She’ll greet you with “Tuturuu~!” and is always ready to chat or cheer you up!

---

## 📸 Screenshots

![Desktop Preview](assets/wallpapers/your-wallpaper.png)
![MayushiAI Terminal](assets/screenshots/mayushiai-terminal.png)

---

## 🧪 Roadmap

- [x] Theming foundation (Plymouth, LightDM, GTK)
- [x] MayushiAI CLI
- [ ] First-boot wizard
- [ ] MayushiAI desktop widget
- [ ] ISO polish & installer slides
- [ ] Community feedback & feature requests

---

## 🧑‍💻 Credits

- **Project Lead:** [@carolynclair](https://github.com/carolynclair)
- **Theme & AI:** Inspired by *Steins;Gate* (© 5pb./Nitroplus)
- **Contributors:** Gary Hancart ~Tuturuu~~

---

## ⚠️ Disclaimer

This project is a fan creation and is not affiliated with or endorsed by 5pb., Nitroplus, or the official Steins;Gate franchise.

---

> “Remember, the universe has a beginning, but it has no end. —Rintarou Okabe”

---
