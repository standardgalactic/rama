def anodize_headline(headline):
    # Simplistic keyword replacement approach
    replacements = {
        'Shocking': 'Surprising',
        'Incredible': 'Noteworthy',
        'Unbelievable': 'Interesting',
        # Add more replacements as needed
    }
    for sensational, mundane in replacements.items():
        headline = headline.replace(sensational, mundane)
    return headline

def blandify_and_decontextualize(data):
    # Existing steps
    if data['age'] < 20:
        data['age'] = '<20'
    elif data['age'] < 40:
        data['age'] = '20-39'
    else:
        data['age'] = '40+'
    data['location'] = data['location'].split(',')[1]  # Assuming format "City,Country"
    data['name'] = 'REDACTED'
    
    # New step: Anodize headline
    if 'headline' in data:  # Assuming there's a 'headline' field to anodize
        data['headline'] = anodize_headline(data['headline'])
    
    return data

# Example data with a sensational headline
user_data = {
    'name': 'Jane Doe',
    'age': 25,
    'location': 'Springfield,USA',
    'headline': 'Shocking Discovery in Springfield!'
}

blandified_and_decontextualized_data = blandify_and_decontextualize(user_data)

print(blandified_and_decontextualized_data)
