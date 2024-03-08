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


if 'tok_' in response.text:
    print("#Aprovadas", sk, "『 ★ SK LIVE ★ 』")
elif 'api_key_expired' in response.text:
    print("#Reprovadas", sk, "『 ★ KEY EXPIRED ★ 』")
elif 'testmode_charges_only' in response.text:
    print("#Reprovadas", sk, "『 ★ TEST MODE CHARGES ONLY ★ 』")
elif 'Invalid API Key' in response.text:
    print("#Reprovadas", sk, "『 ★ INVALID API KEY ★ 』")
elif 'You must pass full card details to create a token.' in response.text:
    print("#Reprovadas", sk, "『 ★ CHANGE CC ★ 』" )    
else:
    print("#Reprovadas", sk, "『 ★ Error Not Listed ★ 』")
