# Subbis

<p align="center">
  <img src="https://img.shields.io/badge/python-3.6+-red.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-white.svg" alt="License">
  <img src="https://img.shields.io/badge/status-active-red.svg" alt="Status">
</p>

## ✨ Features

- **Fast Subdomain Discovery**: Efficiently finds subdomains using DNS resolution
- **Multi-threading**: Configurable concurrent threads for faster scanning
- **Stylish Interface**: Clean and modern red & white themed CLI
- **Progress Tracking**: Real-time scanning progress with visual indicators
- **Flexible Output**: Save results to file or view in terminal
- **User-Friendly**: Clear error messages and intuitive command structure

## 📋 Requirements

- Python 3.6+
- Required packages:
  - dnspython
  - tqdm
  - colorama

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/unkelr/subbis.git
cd subdomain-finder

# Install required packages
pip install -r requirements.txt
```

## 💻 Usage

Basic usage:

```bash
python3 subbis.py example.com -w wordlists/subdomains.txt
```

### Command Line Arguments

```
python3 subbis.py [-h] -w WORDLIST [-t THREADS] [-o OUTPUT] domain
```

| Argument | Description |
|----------|-------------|
| `domain` | Target domain to scan for subdomains |
| `-w, --wordlist` | Path to wordlist file containing potential subdomain names |
| `-t, --threads` | Number of concurrent threads (default: 10) |
| `-o, --output` | Output file to save results |
| `-h, --help` | Show help message |

## 📝 Example

```bash
python3 subbis.py google.com -w wordlists/top1000.txt -t 20 -o results.txt
```

## 📚 Wordlists

The tool requires a wordlist containing potential subdomain names. Some recommended wordlists:

- `wordlists/common.txt` - Common subdomain names (included)
- `wordlists/top1000.txt` - Top 1000 most common subdomains (included)

You can also use popular wordlists from projects like:
- [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)
- [Assetnote Wordlists](https://wordlists.assetnote.io/)

### Integrating with Other Tools

You can pipe the output to other tools:

```bash
python3 subbis.py example.com -w wordlists/common.txt | grep "api" > api_subdomains.txt
```

### Creating a Custom Wordlist

Combine multiple wordlists:

```bash
cat wordlists/*.txt | sort -u > custom_wordlist.txt
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/unkelr/subbis/issues).

## 📊 Roadmap

- [ ] Add support for recursive subdomain enumeration
- [ ] Implement IP resolution for discovered subdomains
- [ ] Add port scanning capabilities
- [ ] Create web interface
- [ ] Support for API keys from various DNS providers

## 📞 Contact

Created by [@unkelr](https://github.com/unkelr) - feel free to reach out!

---

<p align="center">
  Made with ❤️ for the cybersecurity community
</p>
