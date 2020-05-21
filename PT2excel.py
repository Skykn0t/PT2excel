import requests
import xlsxwriter #https://www.geeksforgeeks.org/python-create-and-write-on-excel-file-using-xlsxwriter-module/ & https://xlsxwriter.readthedocs.io/worksheet.html

username = "your RiskIQ username"
key = "Your RiskIQ API key"
auth = (username, key)
api_base = "https://api.passivetotal.org"
#PT_sources = [RESOLUTIONS, WHOIS, CERTIFICATES, SUBDOMAINS, TRACKERS, COMPONENTS, HOST_PAIRS, OSINT, HASHES, DNS, COOKIES]

# User defines the domain they want to get PT data for
print("Welcome to PT2excel! NOTE: Each execution uses ~10 API calls")
target_domain = input("Enter the target domain:")
print(f"Creating an excel spreadsheet for " + target_domain + " ...")

# Creates excel spreadsheet
workbook_name = target_domain + ".xlsx"
workbook = xlsxwriter.Workbook(f"{workbook_name}")
#worksheet_header_format = workbook.add_Format({"bold": True, "font_size": 16})
#column_header_format = workbook.add_format({"bold": True, "font_size": 12, "bg_color": "#808080", "border": 1})
#row = 2
#column = 0

# Gotta figure out how to do this with a loop.
# def excel_setup():
#     for i in PT_sources:
#         (PT_sources[i]) = workbook.add_worksheet()
#         return (PT_sources[i])
# excel_setup()  

# Sets up call to PT API
def PT_get(path, query):
    url = api_base + path
    PT_data = {"query": target_domain}
    response = requests.get(url, auth=auth, json=PT_data)
    return response.json()

# GET Resolutions (Resolve, [[Location]], [[Network]], [[ASN]], First, Last, Source) Note: don't see location feature in docs.. perhaps external API?
# Set up worksheet
RESOLUTIONS_wkst = workbook.add_worksheet("Resolutions")
RESOLUTIONS_wkst.write("A1", "Resolutions")
# Call API
pDNS_results = PT_get("/v2/dns/passive", target_domain)
for resolve in pDNS_results["results"]:
    RESOLUTIONS_wkst.write(2, 3, resolve)
    row += 1
for firstSeen in pDNS_results["results"]:
    RESOLUTIONS_wkst.write(3, 3, firstSeen)
    row += 1
for lastSeen in pDNS_results["results"]:
    RESOLUTIONS_wkst.write(4, 3, lastSeen)
    row += 1
for source in pDNS_results["results"]:
    RESOLUTIONS_wkst.write(3, 0, source)
    row += 1

# GET Whois
# Set up worksheet
WHOIS_wkst = workbook.add_worksheet("WhoIs")
WHOIS_wkst.write("A1", "Whois")
# Call API
whois_results = PT_get("https://api.passivetotal.org/v2/whois", target_domain)


# GET Certificates

# GET Subdomains
# Set up worksheet
SUBDOMAINS_wkst = workbook.add_worksheet("Subdomains")
SUBDOMAINS_wkst.write("A1", "Subdomains")
# Call API
subdomains_results = PT_get("/v2/enrichment/subdomains", target_domain)
for subdomains in subdomains_results["subdomains"]:
    # print(f"Found subdomain: {subdomains}" + "." + target_domain)
    full_subdomain = subdomains + "." + target_domain
    SUBDOMAINS_wkst.write(2, 0, full_subdomain)
    row += 1

# Get Trackers

# GET Components

# GET Host Pairs

# GET OSINT

# GET Hashes

# GET DNS

# GET Cookies


workbook.close()