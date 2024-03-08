import requests


url = 'https://api.stripe.com/v1/tokens'


sk = input("Enter your Stripe API key: ")


card_data = {
    'card': {
        'number': '4912461004526326',
        'exp_month': '04',
        'exp_year': '2024',
        'cvc': '011'
    }
}

response = requests.post(url, auth=(sk, ''), data=card_data)

print(response.text)

credits="Code By Techno Tinker"

if 'tok_' in response.text:
    print("#Aprovadas", sk, "『 ★ SK LIVE ★ 』 " ,credits)
elif 'api_key_expired' in response.text:
    print("#Reprovadas", sk, "『 ★ KEY EXPIRED ★ 』" ,credits)
elif 'testmode_charges_only' in response.text:
    print("#Reprovadas", sk, "『 ★ TEST MODE CHARGES ONLY ★ 』" ,credits)
elif 'Invalid API Key' in response.text:
    print("#Reprovadas", sk, "『 ★ INVALID API KEY ★ 』" ,credits)
elif 'You must pass full card details to create a token.' in response.text:
    print("#Reprovadas", sk, "『 ★ CHANGE CC ★ 』" ,credits)    
else:
    print("#Reprovadas", sk, "『 ★ Error Not Listed ★ 』" ,credits)
