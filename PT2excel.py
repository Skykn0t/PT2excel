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
print(f"Creating an excel spreadsheet for " + target_domain)

# Creates excel spreadsheet
workbook_name = target_domain + ".xlsx"
workbook = xlsxwriter.Workbook(f"{workbook_name}")
SUBDOMAINS_wkst = workbook.add_worksheet("Subdomains")
row = 0
column = 0

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

# GET Resolutions

# GET Whois

# GET Certificates

# GET Subdomains
subdomains_results = PT_get("/v2/enrichment/subdomains", target_domain)
for subdomains in subdomains_results["subdomains"]:
    # print(f"Found subdomain: {subdomains}" + "." + target_domain)
    SUBDOMAINS_wkst.write(row, column, subdomains)
    row += 1

# Get Trackers

# GET Components

# GET Host Pairs

# GET OSINT

# GET Hashes

# GET DNS

# GET Cookies


workbook.close()