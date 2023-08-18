import requests

def gen_quote(user_report_data):
    with open("/dev/attestation/user_report_data", 'w') as urd:
        urd.write(user_report_data)
    
    with open("/dev/attestation/quote", 'r') as quote_file:
        quote = quote_file.readall()
    
    with open("/dev/attestation/report", 'r') as report_file:
        report = report_file.readall()
    
    return quote, report

# def attest_quote(quote):
#     attest_uri = "https://sgxdemoattestation.eus.attest.azure.net/attest/SgxEnclave?api-version=2022-08-01"
    