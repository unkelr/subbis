import argparse
import dns.resolver
import concurrent.futures
import sys
import time
from tqdm import tqdm
from colorama import Fore, Back, Style, init


def print_section(title):
    print(f"\n{Fore.WHITE}╔{'═' * 60}╗")
    print(f"{Fore.WHITE}║ {Fore.RED}{title}{' ' * (59 - len(title))}{Fore.WHITE}║")
    print(f"{Fore.WHITE}╚{'═' * 60}╝")

def print_info(label, value):
    print(f"{Fore.WHITE}[{Fore.RED}•{Fore.WHITE}] {Fore.RED}{label}: {Fore.WHITE}{value}")

def print_success(message):
    print(f"{Fore.WHITE}[{Fore.RED}✓{Fore.WHITE}] {message}")

def print_error(message):
    print(f"{Fore.WHITE}[{Fore.RED}✗{Fore.WHITE}] {Fore.RED}Error: {Fore.WHITE}{message}")

def check_subdomain(subdomain, domain):
    full_domain = f"{subdomain}.{domain}"
    try:
        dns.resolver.resolve(full_domain, 'A')
        return full_domain
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return None
    except Exception as e:
        print_error(f"Checking {full_domain}: {str(e)}")
        return None

def find_subdomains(domain, wordlist_file, threads=10):
    try:
        with open(wordlist_file, 'r') as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print_error(f"Wordlist file '{wordlist_file}' not found.")
        sys.exit(1)
    
    print_info("Scanning", f"{len(subdomains)} potential subdomains")
    
    found_subdomains = []
    
    bar_format = f"{Fore.WHITE}{{l_bar}}{Fore.RED}{{bar}}{Fore.WHITE}{{r_bar}}"
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(check_subdomain, subdomain, domain): subdomain for subdomain in subdomains}
        
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(subdomains), desc="Progress", 
                          bar_format=bar_format, ncols=70):
            result = future.result()
            if result:
                found_subdomains.append(result)
                print(f"\n{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Found: {Fore.RED}{result}")
    
    return found_subdomains

def main():
    parser = argparse.ArgumentParser(description='Find subdomains for a given domain.')
    parser.add_argument('domain', help='Target domain to scan for subdomains')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to wordlist file containing potential subdomain names')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of concurrent threads (default: 10)')
    parser.add_argument('-o', '--output', help='Output file to save results')
    
    args = parser.parse_args()
    
    print("\033c", end="")
    
    print_section("Scan Configuration")
    print_info("Target", args.domain)
    print_info("Wordlist", args.wordlist)
    print_info("Threads", args.threads)
    print_info("Started at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    print_section("Scanning")
    start_time = time.time()
    found_subdomains = find_subdomains(args.domain, args.wordlist, args.threads)
    scan_time = time.time() - start_time
    
    print_section("Results")
    if found_subdomains:
        print_success(f"Found {len(found_subdomains)} subdomains in {scan_time:.2f} seconds")
        
        for subdomain in found_subdomains:
            print(f"{Fore.WHITE}    ├─ {Fore.RED}{subdomain}")
            
        if args.output:
            try:
                with open(args.output, 'w') as output_file:
                    for subdomain in found_subdomains:
                        output_file.write(f"{subdomain}\n")
                print_success(f"Results saved to {args.output}")
            except Exception as e:
                print_error(f"Saving results to file: {str(e)}")
    else:
        print_info("Status", "No subdomains found")
    
    print(f"\n{Fore.WHITE}╔{'═' * 60}╗")
    print(f"{Fore.WHITE}║ {Fore.RED}Scan completed in {scan_time:.2f}       {' ' * (34 - len(f'{scan_time:.2f}'))}{Fore.WHITE}║")
    print(f"{Fore.WHITE}╚{'═' * 60}╝")

if __name__ == "__main__":
    main()
